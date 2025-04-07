import random


class BST:
    def __init__(self):
        self.val: int
        self.val = None
        self.right: BST
        self.right = None
        self.left: BST
        self.left = None


def add_elem(node: BST, new: int):
    if new < node.val:
        if node.left is None:
            node.left = BST()
            node.left.val = new
        else:
            add_elem(node.left, new)
    else:
        if node.right is None:
            node.right = BST()
            node.right.val = new
        else:
            add_elem(node.right, new)
    pass


def print_tree(node: BST, retreat=0):
    if node is not None:
        print(" " * (retreat * 4) + str(node.val))
        if node.left is not None or node.right is not None:
            print_tree(node.left, retreat + 1)
            print_tree(node.right, retreat + 1)
    pass


def count_multiples_of_10(node: BST):
    if node is not None:
        count = 1 if node.val % 10 == 0 else 0
        count += count_multiples_of_10(node.left)
        count += count_multiples_of_10(node.right)
        return count
    return 0


def remove_leaf(node: BST, parent=None, is_left_child=False):
    if node is not None:
        if node.left is None and node.right is None:
            if parent is not None:
                if is_left_child:
                    parent.left = None
                else:
                    parent.right = None
        else:
            remove_leaf(node.left, node, True)
            remove_leaf(node.right, node, False)


if __name__ == "__main__":
    root: BST
    count_nodes: int

    root = BST()
    count_nodes = int(input("Input count nodes:"))
    root.val = int(input("Input root val:"))
    for _ in range(count_nodes):
        new_node = random.randint(0, 100)
        add_elem(root, new_node)

    print("Print tree:")
    print_tree(root)
    print("Number of elements in the tree that are multiples of 10:", count_multiples_of_10(root))
    remove_leaf(root)
    print("Print tree after remove leaf:")
    print_tree(root)
    pass


