def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def binary_search(arr: list, target: int) -> int:
    left: int
    right: int
    mid:int
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# Приклад використання:

if __name__ == "__main__":
    # result: int
    # n: int
    # n = int(input("Введіть індекс числа Фібоначчі: "))
    # result = fibonacci(n)
    # print(f"Число Фібоначчі з індексом {n} дорівнює {result}.")
    arr:list
    target: int
    result: int

    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = int(input("Введіть елемент: "))
    result = binary_search(arr, target)
    if result != -1:
        print(f"Елемент {target} знайдено в позиції {result}.")
    else:
        print(f"Елемент {target} не знайдено.")