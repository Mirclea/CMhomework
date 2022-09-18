import read_data
import sudoku


def main(meta_path, save_path):
    sudokuBoard, list_questions = read_data.read_data(meta_path)
    print("Question:")
    print(sudokuBoard)
    for i in range(5):
        if not sudoku.solve(list_questions[i]):
            print('error!')
    print("Answer:")
    print(sudokuBoard)
    read_data.save_data(sudokuBoard, save_path)


if __name__ == '__main__':
    meta_path1 = './in/input1.txt'
    meta_path2 = './in/input2.txt'

    save_path1 = './out/out1.txt'
    save_path2 = './out/out2.txt'

    main(meta_path1, save_path1)
    main(meta_path2, save_path2)
