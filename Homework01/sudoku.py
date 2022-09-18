# Initialize a 2-D list with initial values described by the problem.
# Returns board
import time


def setBoard(sudokuBoard):
    board = list()
    rows = sudokuBoard.split('\n')
    for row in rows:
        column = list()
        for character in row:
            if character != ' ':
                digit = int(character)
                column.append(digit)
        board.append(column)
    return board[1:10]


# Find next empty space in Sudoku board and return dimensions
def findEmpty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


# Check whether a specific number can be used for specific dimensions
def isValid(board, num, pos):
    row, col = pos
    # Check if all row elements include this number
    for j in range(9):
        if board[row][j] == num:
            return False
    # Check if all column elements include this number
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check if the number is already included in the block
    rowBlockStart = 3 * (row // 3)
    colBlockStart = 3 * (col // 3)

    rowBlockEnd = rowBlockStart + 3
    colBlockEnd = colBlockStart + 3
    for i in range(rowBlockStart, rowBlockEnd):
        for j in range(colBlockStart, colBlockEnd):
            if board[i][j] == num:
                return False
    return True


# Solve Sudoku using backtracking
def solve(board):
    blank = findEmpty(board)
    if not blank:
        return True
    else:
        row, col = blank
    for i in range(1, 10):
        if isValid(board, i, blank):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


if __name__ == "__main__":
    sudokuBoard = '''
     200080300
     060070084
     030500209
     000105408
     000000000
     402706000
     301007040
     720040060
     004010003
     '''
    board = setBoard(sudokuBoard)
    start = time.time()
    print(solve(board))
    for l in board:
        print(l)
    end = time.time()
    print(end - start)
