#-------------Practice lesson 8------------------
def find_num_position(numbers, target):
    positions = []
    for i in range(len(numbers)):
        if numbers[i] == target:
            positions.append(i + 1)
    return positions if positions else None


if __name__ == "__main__":
    # Task 1
    a = list(map(int, input("Enter list: ").split()))
    print("first element:", a[0])
    a.pop(0)
    print("tail:", a)
    # Task 2
    numbers = list(map(int, input("Enter list: ").split()))

    if len(numbers) > 1:
        sums = []
        for i in range(len(numbers)):
            num_left = numbers[(i - 1) % len(numbers)]
            num_right = numbers[(i + 1) % len(numbers)]
            sums.append(num_left + num_right)
        print(*sums)
    else:
        print(numbers[0])
    # Task 3
    list_task_3 = list(map(int, input("Enter list: ").split()))
    target_num = int(input("Enter finder number:"))

    final_list = find_num_position(list_task_3, target_num)
    if final_list:
        print(final_list)
    else:
        print("None")