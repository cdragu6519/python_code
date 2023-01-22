import random

board = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
]
user_board = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
]
letter_to_index = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
}


# go from board coordinates to actual coordinates
# for example 'b3' -> [2,1]
def get_coordinates(c):
    return [int(c[1]) - 1, letter_to_index[c[0]]]


def print_board(board):
    out = '  ABCDE\n'
    i = 1
    for row in board:
        out += str(i) + ' ' + ''.join(map(str, row)) + '\n'
        i = i + 1
    return out

#
# return a list with the coordinates from existing ship
def get_existing_coordinates():
    res = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'S':
                res.append([i, j])
    return res


# add a ship on board if possible
# returns false if failed, true if ship added successfully
def add_ship():
    shipCoords = get_existing_coordinates()
    direction = random.choice(['v', 'h'])
    if direction == 'v':
        x = random.choice([0, 1, 2])
        y = random.choice([0, 1, 2, 3, 4])
        if [x,y] in shipCoords:
            return False
        if [x + 1,y] in shipCoords:
            return False
        if [x + 2,y] in shipCoords:
            return False

        board[x][y] = 'S'
        board[x + 1][y] = 'S'
        board[x + 2][y] = 'S'
    else:
        x = random.choice([0, 1, 2, 3, 4])
        y = random.choice([0, 1, 2])
        if [x,y] in shipCoords:
            return False
        if [x,y + 1] in shipCoords:
            return False
        if [x,y + 2] in shipCoords:
            return False

        board[x][y] = 'S'
        board[x][y + 1] = 'S'
        board[x][y + 2] = 'S'
    print(direction, x, y)
    return True


def is_hit(move):
    xy = get_coordinates(move)
    if board[xy[0]][xy[1]] == 'S':
        return True
    return False


def is_game_over():
    counter_S = 0
    counter_X = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'S':
                counter_S = counter_S + 1
            if user_board[i][j] == 'X':
                counter_X = counter_X + 1
    if counter_X == counter_S:
        return True
    return False


def main():
    add_ship()
    count = 1
    while count < 3:
        if add_ship():
            count = count + 1

    print(print_board(board))
    print(print_board(user_board))

    while not is_game_over():
        move = input('choose your target (lowercase) : ')
        xy = get_coordinates(move)
        if is_hit(move):
            print('successful hit')
            user_board[xy[0]][xy[1]] = 'X'
        else:
            print('you missed')
            user_board[xy[0]][xy[1]] = 'M'
        print(print_board(user_board))

    print('Game over, You won')


if __name__ == "__main__":
    main()
