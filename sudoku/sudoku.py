board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(brd):
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validation(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0

    return False


def validation(brd, number, position):

    for i in range(len(brd[0])):  # Checking row
        if brd[position[0]][i] == number and position[1] != i:
            return False


    for i in range(len(brd)):  #Checking column
        if brd[i][position[1]] == number and position[0] != i:
            return False


    box_x = position[1] // 3  #Checking square
    box_y = position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if brd[i][j] == number and (i, j) != position:
                return False

    return True

def board_division(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str((brd[i][j])   ) + " ", end="")


def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0 :
                return (i, j)
    return None

board_division(board)
solve(board)
print("__________________________")
board_division(board)