import numpy as np
import sudoku


def read_data(path):
    sudokuBoard = []
    with open(path, 'r') as f:
        for line in f:
            line_int = [int(i) for i in line.split(' ')]
            sudokuBoard.append(line_int)

    sudokuBoard = np.array(sudokuBoard)

    sudoku1 = sudokuBoard[:9, :9]
    sudoku2 = sudokuBoard[:9, 12:21]
    sudoku3 = sudokuBoard[12:21, :9]
    sudoku4 = sudokuBoard[12:21, 12:21]
    sudoku5 = sudokuBoard[6:15, 6:15]

    return sudokuBoard, [sudoku1, sudoku2, sudoku3, sudoku4, sudoku5]


def save_data(sudokuBoard, path):
    file = open(path, 'w')
    for line in sudokuBoard:
        for i in line:
            file.write(str(i))
            file.write(" ")
        file.write('\n')


if __name__ == '__main__':
    path = 'in/input2.txt'
    save_path = 'out/out2.txt'
    sudokuBoard, list_questions = read_data(path)
    print(sudokuBoard)
    for i in range(5):
        if not sudoku.solve(list_questions[i]):
            print('error!')
    save_data(sudokuBoard, save_path)
    print(sudokuBoard)
