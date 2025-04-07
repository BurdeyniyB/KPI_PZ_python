class Node:
    def __init__(self, val: int):
        self.next: Node
        self.next = None
        self.val = val


class LinkedList:
    def __init__(self):
        self.__root: Node
        self.__root = None

    def add_head(self, val: int) -> None:
        self.__root = Node(val)

    def append(self, val: int) -> None:
        new_node: Node

        if self.__root is None:
            self.add_head(val)
        else:
            new_node = Node(val)
            current_node = self.__root
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def remove(self, val: int) -> None:
        current_node = self.__root
        previous_node = None

        while current_node:
            if current_node.val == val:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.__root = current_node.next
                break
            previous_node = current_node
            current_node = current_node.next
        if previous_node and previous_node.next:
            next_node = previous_node.next
            temp = Node(previous_node.val)
            temp.next = next_node.next

            current_node = self.__root
            if current_node.val == previous_node.val:
                self.__root = Node(next_node.val)
                self.__root.next = temp
            else:
                while current_node:
                    if current_node.next.val == previous_node.val:
                        current_node.next = previous_node.next
                        current_node = current_node.next
                        break
                    current_node = current_node.next
                current_node.next = temp

    def remove_max_following(self) -> None:
        max_value = float('-inf')
        current_node = self.__root
        prev_node_to_remove = None
        node_to_remove = None
        while current_node:
            if current_node.val > max_value:
                max_value = current_node.val
                prev_node_to_remove = current_node
                node_to_remove = current_node.next
            current_node = current_node.next

        if node_to_remove is not None:
            prev_node_to_remove.next = node_to_remove.next
            del node_to_remove

    def print_list(self) -> None:
        line = ""
        current_node = self.__root
        while current_node:
            line += str(current_node.val) + " "
            current_node = current_node.next
        print(line)
