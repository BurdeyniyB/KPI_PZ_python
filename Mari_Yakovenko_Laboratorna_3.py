import time
import random

chacker = lambda j, half_length: j+1 if (j >= half_length) else j
def choice_matrix_size():
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

def choice_task():
    size = input("Choice task:\n"
                 "1. insertion\n"
                 "2. exchange\n"
                 "your choice: ")
    if size.isdigit() and 0 < int(size) <= 2:
        switch = {
            '1': 1,
            '2': 2
        }
        return switch.get(size)
    print("Incorrect data!")
    return choice_matrix_size()

def show_matrix(matrix):
    show_matrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            show_matrix += "| {:>3} |".format(matrix[i][j])
        show_matrix += "\n"
    print(show_matrix)
def bypass_array(matrix, matrix_size, num_task):
    half_length = int(matrix_size / 2)
    for j in range(0, matrix_size):
        arr = []
        j1 = chacker(j, half_length)
        for i in range(half_length+abs(half_length - j1)-1, matrix_size):
            arr.append(matrix[i][j])
        if num_task == 1:
            exchange_sort(arr)
        else:
            exchange_sort(arr)
        for i in range(half_length+abs(half_length - j1)-1, matrix_size):
            matrix[i][j] = arr[(matrix_size-1)-i]
def exchange_sort(arr):
    length = len(arr)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

matrix_size = choice_matrix_size()
matrix = [[random.randint(1, 10) for _ in range(matrix_size)] for _ in range(matrix_size)]
show_matrix(matrix)
num_task = choice_task()
time_begin = time.perf_counter_ns()
bypass_array(matrix, matrix_size, num_task)
time_after = time.perf_counter_ns()
spend_time = (time_after - time_begin) / 1000000
if num_task == 1:
    print("---------- insertion ----------")
else:
    print("---------- exchange ----------")
show_matrix(matrix)
print(f"Time: {spend_time}")
