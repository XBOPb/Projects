import turtle
import time
import sys
from collections import deque

screen = turtle.Screen()  # Определяем экран программы
screen.bgcolor("grey")    # Определяем фон
screen.title("Maze")      # Определяем название программы
screen.setup(1300, 700)   # Определяем размер окна программы


class Maze(turtle.Turtle):        # Определяем класс лабиринта
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")      # Форма объекта - квадрат
        self.color("white")       # Цвет
        self.penup()              # Чтобы не оставалось следов объекта
        self.speed(0)             # Объект стоит на месте


class Green(turtle.Turtle):       # Класс для обозначения поиска пути
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


class Black(turtle.Turtle):      # Класс для обозначения текущего разветвления
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)


class Red(turtle.Turtle):        # Класс для обозначения начальной точки
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)


class Yellow(turtle.Turtle):     # Класс для обозначения финального кратчайшего пути
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)


# Определяем лабиринт, где "s" - старт, "e" - конец, "+" - стена
grid = [
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
    "+               +                                 +",
    "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
    "+s          +                 +               ++  +",
    "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
    "+  +     +  +           +  +                 +++  +",
    "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
    "+  +  +  +  +  +  +        +  +  +        +       +",
    "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
    "+  +     +  +          +   +           +  +  ++  ++",
    "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
    "+     +  +     +              +              ++   +",
    "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
    "+  +  +                    +     +     +  +  +++  +",
    "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
    "+  +  +     +     +     +  +  +     +     +  ++  ++",
    "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
    "+                       +  +  +              ++  ++",
    "+ ++++++             +  +  +  +  +++        +++  ++",
    "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
    "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
    "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
    "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
    "+      ++ +++++++e+++     ++          ++    +++++++",
    "+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]


def setup_maze(grid):                           # Определяем функцию по рисованию лабиринта
    global start_x, start_y, end_x, end_y       # Устанавливаем глобальные переменные для начала и конца пути
    for y in range(len(grid)):                  # Прочитать каждый ряд
        for x in range(len(grid[y])):           # Прочитать каждый квадрат в ряде
            character = grid[y][x]              # Символ - объект в точке
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":
                path.append((screen_x, screen_y))

            if character == "e":
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x, screen_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def exit_program():
    screen.exitonclick()
    sys.exit()


def search(x, y):
    frontier.append((x, y))
    solution[x, y] = x, y

    while len(frontier) > 0:
        time.sleep(0)
        x, y = frontier.popleft()

        if(x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            solution[cell] = x, y
            black.goto(cell)
            black.stamp()
            frontier.append(cell)
            visited.add((x-24, y))

        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            black.goto(cell)
            black.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))

        if(x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            black.goto(cell)
            black.stamp()
            frontier.append(cell)
            visited.add((x + 24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            black.goto(cell)
            black.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        green.goto(x, y)
        green.stamp()


def backtrack(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]


maze = Maze()
red = Red()
black = Black()
green = Green()
yellow = Yellow()


walls = []
path = []
visited = set()
frontier = deque()
solution = {}


setup_maze(grid)
search(start_x, start_y)
backtrack(end_x, end_y)
screen.exitonclick()
