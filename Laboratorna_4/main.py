import string

from LinkedList import LinkedList
from DoubleList import DoubleList


def check_digit() -> int:
    choice = input("Enter a number: ")
    if choice.isdigit():
        return int(choice)
    print("Incorrect data!")
    return check_digit()


def fill_list(curr_list, name: string) -> None:
    count_elements: int
    element: int

    print(f"Enter the number of elements for the {name}:")
    count_elements = check_digit()
    print(f"Enter the elements for the {name}:")
    for _ in range(count_elements):
        element = check_digit()
        curr_list.append(element)
    print("Linked List:")
    curr_list.print_list()


def destroy_element(curr_list, name: string) -> None:
    key_remove: int

    print(f"Enter the key to remove from the {name}:")
    key_remove = check_digit()
    curr_list.remove(key_remove)
    print(f"{name} after removing the element with the specified key:")
    curr_list.print_list()


def variant_task(curr_list, name: string) -> None:
    curr_list.remove_max_following()
    print(f"{name} after removing the element following the first maximum value:")
    curr_list.print_list()


if __name__ == "__main__":
    linked_list: LinkedList
    double_list: DoubleList

    linked_list = LinkedList()
    double_list = DoubleList()

    # Linkedlist
    fill_list(linked_list, "linked list")
    destroy_element(linked_list, "linked list")
    variant_task(linked_list, "linked list")

    # DoubleList
    fill_list(double_list, "double list")
    destroy_element(double_list, "double list")
    variant_task(double_list, "double list")
