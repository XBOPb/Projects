import sys

import pygame
import random

LIGHTBLUE = (176, 224, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 800
HEIGHT = 600
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img='pepeIcon.png'):
        super().__init__()                      # Вызов конструктора родительского класса

        self.image = pygame.image.load(img).convert_alpha()  # Загружаем изображение, убираем квадратные поля картинки
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0                       # Установка вектора скорости
        self.change_y = 0
        self.walls = None

        self.coins = None                       # Добавим монетки в класс
        self.collected_coins = 0

        self.home = pygame.sprite.GroupSingle()
        self.win = False

        self.enemies = pygame.sprite.Group()    # Добавим врагов
        self.alive = True                       # Игрок жив если не встретился с врагом

    def update(self):                           # Функция обновления состояния
        self.rect.x += self.change_x            # Движение игрока влево-вправо
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)  # Проверка на столкновение со стеной

        for block in block_hit_list:            # Возвращение игрока за границу препятствия, в которое он врезался
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y           # Движение игрока вверх-вниз
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)  # Проверка на столкновение со стеной

        for block in block_hit_list:            # Возвращение игрока за границу препятствия, в которое он врезался
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        coins_hit_list = pygame.sprite.spritecollide(self, self.coins, False)  # Подбор монеток
        for btc in coins_hit_list:
            self.collected_coins += 1            # Подсчет собранных монеток
            btc.kill()                          # Убираем монетку с экрана при подборе

        if pygame.sprite.spritecollideany(self, self.enemies):           # Столкновение с противником
            self.alive = False
        if pygame.sprite.spritecollideany(self, self.home):
            self.win = True


class Wall(pygame.sprite.Sprite):                # Создаем класс стены
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)                   # Красим стены в черный
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Coin(pygame.sprite.Sprite):                # Создаем класс монет
    def __init__(self, x, y, img="coin.png"):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()  # Загружаем изображение в спрайт
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Home(pygame.sprite.Sprite):                # Создаем класс дом
    def __init__(self, x, y, img="home.png"):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()  # Загружаем изображение в спрайт
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):                  # Создаем класс противника
    def __init__(self, x, y, img="yoba.png"):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()  # Загружаем изображение в спрайт
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.start = x                              # Путь противника до случаной точки
        self.stop = x + random.randint(180, 240)
        self.direction = 1                          # Направление противника

    def update(self):
        if self.rect.x >= self.stop:                # Противник поворачивает, когда доходит до точки назначения
            self.rect.x = self.stop
            self.direction = -1
        if self.rect.x <= self.start:               # Противник поворачивает обратно
            self.rect.x = self.start
            self.direction = 1

        self.rect.x += self.direction * 2           # Смещение противника в указнном направлении


pygame.init()                                       # Инициализация окна программы
screen = pygame.display.set_mode([WIDTH, HEIGHT])   # Задание параметров экрана
pygame.display.set_caption('Лабиринт')              # Название имени окна

all_sprite_list = pygame.sprite.Group()             # Переменная для всех спрайтов
wall_list = pygame.sprite.Group()                   # Переменная для спрайтов стен

wall_position = [                                   # Задаем расположение стен
    [0, 0, 10, 600],
    [790, 0, 10, 600],
    [10, 0, 790, 10],
    [0, 200, 100, 10],
    [0, 590, 600, 10],
    [450, 100, 10, 600],
    [550, 450, 250, 10],
    [550, 250, 300, 10],
    [230, 0, 10, 500]
]
for pos in wall_position:                           # Добавляем стены в список спрайтов
    wall = Wall(pos[0], pos[1], pos[2], pos[3])
    wall_list.add(wall)
    all_sprite_list.add(wall)


coins_list = pygame.sprite.Group()
coins_pos = [[50, 550], [750, 50], [750, 300]]      # Задаем расположение монет
for pos in coins_pos:                               # Добавляем монеты в список спрайтов
    coin = Coin(pos[0], pos[1])
    coins_list.add(coin)
    all_sprite_list.add(coin)


enemies_list = pygame.sprite.Group()
enemies_pos = [[10, 500], [400, 50], [400, 400]]                # Задаем расположение врагов
for pos in enemies_pos:                             # Добавляем врагов в список спрайтов
    enemy = Enemy(pos[0], pos[1])
    enemies_list.add(enemy)
    all_sprite_list.add(enemy)


home = Home(650, 500)                               # Задаем расположение дома
all_sprite_list.add(home)                           # Добавляем дом  в список спрайтов


player = Player(50, 50)                             # Добавляем игрока
player.walls = wall_list                            # Проверка столкновения игрока со стеной
all_sprite_list.add(player)                         # Добавляем игрока в список спрайтов
player.coins = coins_list                           # Добавляем список монет в атрибут игрока
player.enemies = enemies_list                       # Добавляем список врагов в атрибут игрока


font = pygame.font.SysFont("Calibri", 40, True)             # Добавляем сообщения для игрока
text_lose = font.render("Вы проиграли!", True, BLACK)       # Сообщение при проигрыше
image_lose = pygame.image.load("angrypepe.png")
text_win = font.render("Вы прошли лабиринт!", True, BLACK)  # Сообщение при победе
image_win = pygame.image.load("pepewin.png")
three_stars_text = font.render("Вы прошли лабиринт и разбогатели!", True, BLACK)  # Собрано 3 монеты
image_three_starts_win = pygame.image.load("richpepe.png")
restart_text = font.render("Нажмите пробел чтобы сыграть заново", True, BLACK)    # Рестарт

time = pygame.time.Clock()


while True:                                    # Прописываем управление игроком
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x = -3
            if event.key == pygame.K_RIGHT:
                player.change_x = 3
            if event.key == pygame.K_UP:
                player.change_y = -3
            if event.key == pygame.K_DOWN:
                player.change_y = 3
            if event.key == pygame.K_DOWN:
                player.change_y = 3
            if event.key == pygame.K_SPACE:
                """
                Далее пришлось поместить код игры в повтор программы, в функцию спрятать его не получается
                """
                pygame.init()  # Инициализация окна программы
                screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Задание параметров экрана
                pygame.display.set_caption('Лабиринт')  # Название имени окна

                all_sprite_list = pygame.sprite.Group()  # Переменная для всех спрайтов
                wall_list = pygame.sprite.Group()  # Переменная для спрайтов стен

                wall_position = [  # Задаем расположение стен
                    [0, 0, 10, 600],
                    [790, 0, 10, 600],
                    [10, 0, 790, 10],
                    [0, 200, 100, 10],
                    [0, 590, 600, 10],
                    [450, 100, 10, 600],
                    [550, 450, 250, 10],
                    [550, 250, 300, 10],
                    [230, 0, 10, 500]
                ]
                for pos in wall_position:  # Добавляем стены в список спрайтов
                    wall = Wall(pos[0], pos[1], pos[2], pos[3])
                    wall_list.add(wall)
                    all_sprite_list.add(wall)

                coins_list = pygame.sprite.Group()
                coins_pos = [[50, 550], [750, 50], [750, 300]]  # Задаем расположение монет
                for pos in coins_pos:  # Добавляем монеты в список спрайтов
                    coin = Coin(pos[0], pos[1])
                    coins_list.add(coin)
                    all_sprite_list.add(coin)

                enemies_list = pygame.sprite.Group()
                enemies_pos = [[10, 500], [400, 50], [400, 400]]   # Задаем расположение врагов
                for pos in enemies_pos:  # Добавляем врагов в список спрайтов
                    enemy = Enemy(pos[0], pos[1])
                    enemies_list.add(enemy)
                    all_sprite_list.add(enemy)

                home = Home(650, 500)
                all_sprite_list.add(home)

                player = Player(50, 50)  # Добавляем игрока
                player.walls = wall_list  # Проверка столкновения игрока со стеной
                all_sprite_list.add(player)  # Добавляем игрока в список спрайтов
                player.coins = coins_list  # Добавляем список монет в атрибут игрока
                player.enemies = enemies_list  # Добавляем список врагов в атрибут игрока

                font = pygame.font.SysFont("Calibri", 40, True)  # Добавляем сообщения для игрока
                text_lose = font.render("Вы проиграли!", True, BLACK)  # Сообщение при проигрыше
                image_lose = pygame.image.load("angrypepe.png")
                text_win = font.render("Вы прошли лабиринт!", True, BLACK)  # Сообщение при победе
                image_win = pygame.image.load("pepewin.png")
                three_stars_text = font.render("Вы прошли лабиринт и разбогатели!", True, BLACK)  # Собрано 3 монеты
                image_three_starts_win = pygame.image.load("richpepe.png")
                restart_text = font.render("Нажмите пробел чтобы сыграть заново", True, BLACK)

                time = pygame.time.Clock()

        elif event.type == pygame.KEYUP:    # Прописываем остановку персонажа при отпущенной клавише движения
            if event.key == pygame.K_LEFT:
                player.change_x = 0
            if event.key == pygame.K_RIGHT:
                player.change_x = 0
            if event.key == pygame.K_UP:
                player.change_y = 0
            if event.key == pygame.K_DOWN:
                player.change_y = 0

    screen.fill(LIGHTBLUE)  # Фон

    if not player.alive:    # Сценарий при смерти игрока
        screen.blit(text_lose, (270, 100))
        screen.blit(image_lose, (250, 200))
        screen.blit(restart_text, (50, 550))
    elif player.rect.colliderect(home) and player.collected_coins < 3:  # Сценарий при смерти игрока, монет меньше трех
        screen.blit(text_win, (220, 100))
        screen.blit(image_win, (260, 200))
        screen.blit(restart_text, (50, 550))
    elif player.rect.colliderect(home) and player.collected_coins == 3: # Сценарий при смерти игрока, все монеты собраны
        screen.blit(three_stars_text, (110, 100))
        screen.blit(image_three_starts_win, (260, 200))
        screen.blit(restart_text, (50, 550))
    else:
        all_sprite_list.update()
        all_sprite_list.draw(screen)

    pygame.display.flip()   # Обновление содержимого экрана
    time.tick(FPS)


