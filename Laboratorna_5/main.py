import random
import string

from merge_sort import merge_sort


def show_matrix(matrix: list[list[int]]) -> None:
    show_matrix: string
    show_matrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            show_matrix += "| {:>2} |".format(matrix[i][j])
        show_matrix += "\n"
    print(show_matrix)


def sparse_matrix_to_list(matrix):
    sparse_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                sparse_list.append((i, j, matrix[i][j]))
    return sparse_list


def create_sparse_matrix(size: int, density=0.3) -> list[list[int]]:
    csm_matrix = []
    for i in range(size):
        row = [0] * size
        for j in range(size):
            if random.random() < density:
                row[j] = random.randint(1, 10)
        csm_matrix.append(row)
    return csm_matrix


def sort_even_rows(matrix: list[list[int]]):
    for i in range(len(matrix)):
        if i % 2 != 0:
            merge_sort(matrix[i])


if __name__ == "__main__":
    matrix_size = int(input("Enter size of matrix: "))

    matrix = create_sparse_matrix(matrix_size)
    sparse_list = sparse_matrix_to_list(matrix)
    print("Matrix before sorting:")
    show_matrix(matrix)
    print("Compressed matrix")
    for row in sparse_list:
        print(row)
    sort_even_rows(matrix)
    print("Matrix after sorting:")
    show_matrix(matrix)
    sparse_list = sparse_matrix_to_list(matrix)
    print("Compressed sort matrix")
    for row in sparse_list:
        print(row)
