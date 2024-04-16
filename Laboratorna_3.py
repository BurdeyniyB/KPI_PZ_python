import string
import time
import random

def choice_matrix_size() -> int:
    size = input("Choice size matrix:\n"
                 "1. 10x10\n"
                 "2. 50x50\n"
                 "your choice: ")
    if size.isdigit() and 0 < int(size) <= 2:
        switch = {
            '1': 10,
            '2': 50
        }
        return switch.get(size)
    print("Incorrect data!")
    return choice_matrix_size()

def choice_task() -> int:
    size = input("Choice task:\n"
                 "1. exchange\n"
                 "2. merge\n"
                 "your choice: ")
    if size.isdigit() and 0 < int(size) <= 2:
        switch = {
            '1': 1,
            '2': 2
        }
        return switch.get(size)
    print("Incorrect data!")
    return choice_matrix_size()

def show_matrix(matrix: list[list[int]]) -> None:
    show_matrix: string
    show_matrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            show_matrix += "| {:>3} |".format(matrix[i][j])
        show_matrix += "\n"
    print(show_matrix)

def bypass_array(matrix: list[list[int]], matrix_size: int, num_task: int) -> None:
    length: int
    length = matrix_size
    arr: list[int]
    for j in range(0, length):
        arr = []
        for i in range(j, length):
            arr.append(matrix[i][j])
        if(num_task == 1):
            exchange_sort(arr)
        else:
            merge_sort(arr)
        for i in range(j, length):
            matrix[i][j] = arr[i-j]

def exchange_sort(arr: list[int]) -> None:
    length: int
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

def merge_sort(arr: list[int]) -> None:
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    # Matrix data
    matrix_size: int
    matrix: list[list[int]]
    # Time
    time_begin: int
    time_after: int
    spend_time: float

    num_task: int

    matrix_size = choice_matrix_size()
    matrix = [[random.randint(1, 10) for _ in range(matrix_size)] for _ in range(matrix_size)]
    show_matrix(matrix)
    num_task = choice_task()
    time_begin = time.perf_counter_ns()
    bypass_array(matrix, matrix_size, num_task)
    time_after = time.perf_counter_ns()
    spend_time = (time_after - time_begin) / 1000000
    if(num_task == 1):
        print("---------- exchange ----------")
    else:
        print("---------- merge ----------")
    show_matrix(matrix)
    print(f"Time: {spend_time}")