from Stack import Stack

def print_stack(stack: Stack):
    if stack.empty():
        print("Stack is empty")
    else:
        print("Stack's elements:")
        for item in stack.items:
            print(item)

def sum(stack: Stack) -> int:
    sum = 0
    for item in stack.items:
        if item >= 15:
            sum += item
    return sum

def insert_symbol(stack: Stack):
    symbol = "$"
    length = len(stack.items)
    middle_index = length // 2
    if length % 2 == 0:
        stack.items.insert(middle_index, symbol)
    else:
        stack.items.insert(middle_index+1, symbol)


if __name__ == "__main__":
    stack = Stack()
    num_elements = int(input("How many element do you want to add to list? "))
    for i in range(0, num_elements):
        element = float(input("input element:"))
        stack.push(element)
    print(f"sum greater than 15: {sum(stack)}")
    insert_symbol(stack)
    print_stack(stack)

