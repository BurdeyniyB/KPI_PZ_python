# ---------Practice lesson №2---------
import string

# The variables for task
# 1.
choise: string
inncorect_answer = True
# 2.
a: int
b: int
c: int
s: int
tax: float
# 3.
index: float
weight: float
height: float

# Task 1
while (inncorect_answer):
    choise = input("choise system:\n"
                   "1. Windows\n"
                   "2. Linux\n"
                   "3. MacOS\n")
    if choise.isdigit() and 0 < int(choise) <= 4:
        switch = {
            1: "Windows",
            2: "Linux",
            3: "MacOS"
        }
        print(f"Your answer: {switch.get(int(choise))}")
        inncorect_answer = False
    else:
        print("Incorect data!")
# Task 2
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
s = int(input("s: "))

if a < s <= b:
    tax = float(s * 0.1)
elif b < s <= c:
    tax = float(s * 0.25)
elif c < s:
    tax = float(s * 0.5)
else:
    tax = 0
print(f"tax: {tax}")

# Task 3
weight = float(input("weight: "))
height = float(input("height: "))
index = weight / (height * height)
if 0 < index < 18.5:
    print("underweight")
elif 18.5 <= index <= 24.9:
    print("normal weight")
elif 24.9 < index:
    print("overweight")
else:
    print("inputed incorect data")
