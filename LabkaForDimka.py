import random
import string
import time


def show_matrix(matrix: list[list[int]]) -> None:
    show_matrix: string
    show_matrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            show_matrix += "| {:>3} |".format(matrix[i][j])
        show_matrix += "\n"
    print(show_matrix)


def task2(matrix: list[list[int]]) -> None:
    replacement_matrix = [[0] * int(len(matrix)) for _ in range(int(len(matrix)))]

    for i in range(int((len(matrix)+1)/2)):
        for j in range(i, len(matrix) - i):
            replacement_matrix[i][j] = matrix[i][j]
    show_matrix(replacement_matrix)
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            matrix[i][j] = matrix[j][i]

    # for i in range(len(replacement_matrix)):
    #     for j in range(len(replacement_matrix)):
    #         matrix[i + len(replacement_matrix)][j + len(replacement_matrix)] = replacement_matrix[i][j]

    print("Changed matrix:")
    show_matrix(matrix)


if __name__ == "__main__":
    matrix = [[random.randint(1, 10) for _ in range(10)] for _ in range(10)]
    show_matrix(matrix)
    task2(matrix)
