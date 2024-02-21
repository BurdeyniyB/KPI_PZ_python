import random
import string
import time


def choice_matrix_size() -> int:
    size = input("Choice size matrix:\n"
                 "1.10x10\n"
                 "2. 50x50\n"
                 "3. 100x100\n"
                 "4. 500x500\n"
                 "your choice: ")
    if size.isdigit() and 0 < int(size) <= 4:
        switch = {
            '1': 10,
            '2': 50,
            '3': 100,
            '4': 500
        }
        return switch.get(size)
    print("Incorect data!")
    return choice_matrix_size()


def get_choose_task() -> int:
    choose = input("Choose task:\n"
                   "1 - TASK 1\n"
                   "2 - TASK 2\n")
    if choose.isdigit() and 1 <= int(choose) <= 2:
        return int(choose)
    print("Incorect data!")
    return get_choose_task()


def show_matrix(matrix: list[list[int]]) -> None:
    show_matrix: string
    show_matrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            show_matrix += "| {:>3} |".format(matrix[i][j])
        show_matrix += "\n"
    print(show_matrix)


def task1(matrix: list[list[int]]) -> None:
    save = [[0] * len(matrix) for _ in range(len(matrix))]
    ind = 0
    need_row = 0
    need_column = 0
    max_sequence: int
    iteration = 0

    for i in range(len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[i][j] < matrix[i][j - 1]:
                save[i][ind] += 1
            else:
                ind += 1
            iteration += 1
        ind = 0
    max_sequence = save[0][0]


    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if save[i][j] > max_sequence:
                max_sequence = save[i][j]
                need_row = i + 1
            iteration += 1
    print(f"row with the most many sequence: {need_row}")
    save = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[j - 1][i] < matrix[j][i]:
                save[ind][i] += 1
            else:
                ind += 1
            iteration += 1
        ind = 0
    max_sequence = save[0][0]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (save[i][j] > max_sequence):
                max_sequence = save[i][j]
                need_column = j + 1
            iteration += 1
    print(f"column with the most many sequence: {need_column}")
    print(f"Iteration: {iteration}")


def task2(matrix: list[list[int]]) -> None:
    replacement_matrix = [[0] * int(len(matrix) // 2) for _ in range(int(len(matrix) // 2))]
    iteration = 0

    for i in range(len(replacement_matrix)):
        for j in range(len(replacement_matrix)):
            replacement_matrix[i][j] = matrix[i][j]
            iteration += 1
    for i in range(len(replacement_matrix)):
        for j in range(len(replacement_matrix)):
            matrix[i][j] = matrix[i + len(replacement_matrix)][j + len(replacement_matrix)]
            iteration += 1
    for i in range(len(replacement_matrix)):
        for j in range(len(replacement_matrix)):
            matrix[i + len(replacement_matrix)][j + len(replacement_matrix)] = replacement_matrix[i][j]
            iteration += 1
    print("Changed matrix:")
    show_matrix(matrix)
    print(f"Iteration: {iteration}")


if __name__ == "__main__":
    # Matrix data
    matrix_size: int
    matrix: list[list[int]]

    # For control spend time
    time_begin: int
    time_after: int
    spend_time: int

    # Choise
    choise_task: int

    matrix_size = choice_matrix_size()
    print(matrix_size)
    matrix = [[random.randint(1, 10) for _ in range(matrix_size)] for _ in range(matrix_size)]
    print("Started matrix:")
    show_matrix(matrix)
    choise_task = get_choose_task()
    time_begin = time.perf_counter_ns()
    if choise_task == 1:
        task1(matrix)
    else:
        task2(matrix)
    time_after = time.perf_counter_ns()
    spend_time = time_after - time_begin
    print(f"Time: {spend_time}")
