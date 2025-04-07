import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def swap_nodes(self, node1, node2):
        node1.data, node2.data = node2.data, node1.data

    def delete_and_swap(self, key):
        if not self.head:
            print("Список порожній.")
            return

        prev_node = None
        current = self.head

        while current:
            if current.data == key:
                if prev_node:
                    prev_node.next = current.next
                    if current.next:
                        prev_node.data, current.next.data = current.next.data, prev_node.data
                    return
                else:
                    print("Немає попереднього вузла для обміну.")
                    return
            prev_node = current
            current = current.next

        print("Ключ не знайдено в списку.")

    def display_ordered(self, A):
        current = self.head
        less = ""
        next = ""
        while current:
            if current.data < A:
                less += str(current.data) + " "
            else:
                next += str(current.data) + " "
            current = current.next
        print(less + next)


class DoublyNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def swap_nodes(self, node1, node2):
        node1.data, node2.data = node2.data, node1.data

    def delete(self, key):
        if not self.head:
            print("Список порожній.")
            return

        current = self.head

        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

        print("Ключ не знайдено в списку.")

    def display_ordered(self, A):
        current = self.head
        less = ""
        next = ""
        while current:
            if current.data < A:
                less += str(current.data) + " "
            else:
                next += str(current.data) + " "
            current = current.next
        print(less + next)


if __name__ == "__main__":
    singleLinkedList = LinkedList()
    doublyLinkedList = DoublyLinkedList()


    n = int(input("Введіть кількість елементів у списку: "))
    for _ in range(n):
        element = random.randint(0, 100)
        singleLinkedList.append(element)
        doublyLinkedList.append(element)

    print("Початковий однозв'язний список:")
    singleLinkedList.display()
    print("Початковий двозв'язний список:")
    doublyLinkedList.display()

    key = int(input("Введіть ключ для видалення та обміну елементів: "))
    singleLinkedList.delete_and_swap(key)
    print("Однозв'язний список після видалення та обміну:")
    singleLinkedList.display()

    key = int(input("Введіть ключ для видалення з двозв'язного списку: "))
    doublyLinkedList.delete(key)
    print("Двозв'язний список після видалення:")
    doublyLinkedList.display()

    A = int(input("Введіть значення A: "))
    print("Елементи однозв'язного списку спочатку всi числа, меншi за A, потiм числа всi iншi числа:")
    singleLinkedList.display_ordered(A)
    A = int(input("Введіть значення A: "))
    print("Елементи двозв'язного списку спочатку всi числа, меншi за A, потiм числа всi iншi числа:")
    doublyLinkedList.display_ordered(A)
