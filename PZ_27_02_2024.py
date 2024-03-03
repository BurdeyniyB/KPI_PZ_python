# ---------Practice lesson №3---------
def task1_sort(a) -> None:
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print("Відсортований список", b)


def input_list() -> list[int]:
    n = int(input("Введіть кількість елементів у списку: "))
    a = []
    for i in range(n):
        element = int(input(f"Введіть {i + 1}-й елемент: "))
        a.append(element)
    return a


def get_next_day(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month < 1 or month > 12 or day < 1 or day > 31:
        return None

    if day == days_in_month[month - 1]:
        day = 1
        month += 1
        if month == 13:
            month = 1
            year += 1
    else:
        day += 1

    return year, month, day


def input_date():
    year = month = day = None
    while year is None or month is None or day is None:
        year = input("Введіть рік (у форматі YYYY): ")
        month = input("Введіть місяць (у форматі MM): ")
        day = input("Введіть день (у форматі DD): ")

        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            print("Помилка: Рік, місяць та день повинні бути числами.")
            year = month = day = None
        else:
            year, month, day = int(year), int(month), int(day)
            if month < 1 or month > 12 or day < 1 or day > 31:
                print("Помилка: Некоректна дата.")
                year = month = day = None

    return year, month, day


if __name__ == "__main__":
    list1: list[int]
    list2: list[int]

    list1 = input_list()
    task1_sort(list1)

    list2 = input_list()
    cubed_list = list(map(lambda x: x ** 3, list2))
    print("Список кубів цілих чисел:", cubed_list)

    year, month, day = input_date()
    next_day = get_next_day(year, month, day)

    if next_day:
        print(f"Наступний день: {next_day[0]:04d}-{next_day[1]:02d}-{next_day[2]:02d}")
    else:
        print("Некоректна дата. Спробуйте ще раз.")
