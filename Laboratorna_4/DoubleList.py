class Node:
    def __init__(self, val: int):
        self.next: Node
        self.next = None
        self.prev: Node
        self.prev = None
        self.val = val


class DoubleList:
    def __init__(self):
        self.__root: Node
        self.__root = None
        self.__next = None

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
            new_node.prev = current_node

    def remove(self, val: int) -> None:
        current_node = self.__root

        while current_node:
            if current_node.val == val:
                if current_node.prev:
                    current_node.next.prev = current_node.prev
                    current_node.prev.next = current_node.next
                else:
                    current_node.prev = None
                    self.__root = current_node.next
                break
            current_node = current_node.next

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
        line_forward = ""
        line_backward = ""
        current_node = self.__root
        while current_node:
            line_forward += str(current_node.val) + " "
            current_node = current_node.next

        current_node = self.__root
        while current_node.next:
            current_node = current_node.next
        while current_node:
            line_backward += str(current_node.val) + " "
            current_node = current_node.prev

        print("Forward:", line_forward)
        print("Backward:", line_backward)
