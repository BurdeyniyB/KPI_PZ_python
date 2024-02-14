import random


#input info about matrix
def choice_matrix_size() -> int:
    size = input("Choice size matrix:\n"
          "1. 10x10\n"
          "2. 50x50\n"
          "3. 100x100\n"
          "4. 500x500\n"
          "your choice: ")
    if size.isdigit() and 0 < int(size)  <= 4:
        switch = {
            '1' : 10,
            '2' : 50,
            '3' : 100,
            '4' : 500
        }
        return switch.get(size)
    print("Incorect data!")
    return choice_matrix_size()

def choose_task() -> int:
    choose = input("Choose task:\n"
                        "1 - TASK 1\n"
                        "2 - TASK 2\n")
    if choose.isdigit() and 1 <= int(choose) <= 2:
        return choose
    print("Incorect data!")
    return choose_task()

def show_matrix(matrix:list[list[int]]) -> None:
    show_matrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            show_matrix += "| {:>3} |".format(matrix[i][j])
        show_matrix += "\n"
    print(show_matrix)

def task1(matrix:list[list[int]]) -> None:
    save = [[0] * len(matrix) for _ in range(len(matrix))]
    ind = 0
    need_row = 0
    need_column = 0
    max_sequence:int

    for i in range(len(matrix)):
        for j in range(1, len(matrix)):
            if(matrix[i][j] < matrix[i][j-1]):
                save[i][ind] += 1
            else:
                ind += 1
        ind = 0
    max_sequence = save[0][0]
    #show_matrix(save)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(save[i][j] > max_sequence):
                max_sequence = save[i][j]
                need_row = i + 1
    print(f"row with the most many sequence: {need_row}")
    save = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(1, len(matrix)):
            if(matrix[j-1][i] < matrix[j][i]):
                save[ind][i] += 1
            else:
                ind += 1
        ind = 0
    max_sequence = save[0][0]
    #show_matrix(save)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(save[i][j] > max_sequence):
                max_sequence = save[i][j]
                need_column = j + 1
    print(f"column with the most many sequence: {need_column}")

def task2(matrix:list[list[int]]) -> None:
    replacement_matrix = [[0] * int(len(matrix)//2) for _ in range(int(len(matrix)//2))]
    for i in range(len(replacement_matrix)):
        for j in range(len(replacement_matrix)):
            replacement_matrix[i][j] = matrix[i][j]
    show_matrix(replacement_matrix)




if __name__ == "__main__":
    matrix_size = choice_matrix_size()
    print(matrix_size)
    matrix = [[random.randint(1, 10) for _ in range(matrix_size)] for _ in range(matrix_size)]
    print("Started matrix:")
    show_matrix(matrix)
    choose = choose_task()
    if(choose == 1):
        task1(matrix)
    else:
        task2(matrix)

