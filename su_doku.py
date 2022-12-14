def is_number_in_row(trial_board: list[list[int]], number: int, print_row: int) -> bool:
    for i in range(9):
        if trial_board[print_row][i] == number:
            return True
    return False


def is_number_in_column(trial_board: list[list[int]], number: int, column: int) -> bool:
    for i in range(9):
        if trial_board[i][column] == number:
            return True
    return False


def is_number_in_box(trial_board: list[list[int]], number: int, print_row: int, column: int) -> bool:
    local_box_row = print_row - print_row % 3
    local_box_column = column - column % 3
    for i in range(local_box_row, local_box_row + 3):
        for j in range(local_box_column, local_box_column + 3):
            if trial_board[i][j] == number:
                return True
    return False


def is_valid_placement(trial_board: list[list[int]], number: int, print_row: int, column: int) -> bool:
    return is_number_in_row(trial_board, number, print_row) or is_number_in_box(trial_board, number, print_row,
                                                                                column) or is_number_in_column(
        trial_board, number, column)


def solve_board(trial_board: list) -> bool:
    for print_row in range(9):
        for column in range(9):
            if trial_board[print_row][column] == 0:
                for number_to_try in range(1, 10):
                    if not is_valid_placement(trial_board, number_to_try, print_row, column):
                        trial_board[print_row][column] = number_to_try
                        if solve_board(trial_board):
                            return True
                        else:
                            trial_board[print_row][column] = 0

                return False
    return True


def print_board(trial_board: list) -> None:
    for print_row in range(9):
        if print_row % 3 == 0 and print_row != 0:
            print("------------")
        for column in range(9):
            if column % 3 == 0 and column != 0:
                print("|", end="")
            print(trial_board[print_row][column], end="")
        print("\n")


def top_left_number(trial_board: list):
    number = str(trial_board[0][0]) + str(trial_board[0][1]) + str(trial_board[0][2])
    return int(number)


all_board = []
board = []
count = 0
with open('p096_sudoku.txt') as f:
    for x in f:
        x = x.rstrip()
        if x.startswith("Grid "):
            all_board.append(board)
            board = []
        else:
            row = [int(i) for i in x]
            board.append(row)
all_board.append(board)

for test_board in all_board:
    solve_board(test_board)

    count += top_left_number(test_board)
print(count)
