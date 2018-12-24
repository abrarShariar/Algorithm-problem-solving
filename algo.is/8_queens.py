
board = [
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""]
]

def update_board (board, i, j):
    new_board = board
    # for horizontal right
    x,y = i, j + 1
    while y < 8:
        if new_board[x][y] != 'X':
            new_board[x][y] = 'X'
        y += 1

    # for horizontal left
    x,y = i, j - 1
    while y >= 0:
        if new_board[x][y] != 'X':
            new_board[x][y] = 'X'
        y -= 1

    # vertical top
    x, y = i - 1, j
    while x >= 0:
        if new_board[x][y] != 'X':
            new_board[x][y] = 'X'
        x -= 1

    # vertical bottom
    x, y = i + 1, j
    while x < 8:
        if new_board[x][y] != 'X':
            new_board[x][y] = 'X'
        x += 1

    # diagonal top right
    x,y = i - 1, j + 1
    while x >= 0 and y < 8:
        if new_board[x][y] != 'X':
            new_board[x][y] = 'X'
        x = x - 1
        y = y + 1

    # diagonal top left
    x,y = i - 1, j - 1
    while x >= 0 and y >= 0:
        if new_board[x][y] != 'X':
            new_board[x][y] = 'X'
        x = x - 1
        y = y - 1

    # diagonal bottom right
    x,y = i + 1, j + 1
    while x < 8 and y < 8:
        if new_board[x][y] != 'X':
            new_board[x][y] = 'X'
        x = x + 1
        y = y + 1

    # diagonal bottom left
    x,y = i + 1, j - 1
    while x < 8 and y >= 0:
        if new_board[x][y] != 'X':
            new_board[x][y] = 'X'
        x = x + 1
        y = y - 1

    return new_board

# input
def run ():
    global board
    for i in range(8):
        line = input()
        for j in range(len(line)):
            if board[i][j] == 'X' and line[j] == '*':
                return False
            else:
                board[i][j] = line[j]

            if line[j] == '*':
                board = update_board(board, i, j)
    return True

result = run()
if result == True:
    print("valid")
else:
    print("invalid")
