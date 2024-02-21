#---------Practice lesson №1---------
# The variables for task
#1.
sum=0
#2.
my_variant = 4
number = my_variant + 25
#3.
time_cycle = 24
current_time = 6
time_before = 10
incorrect_time = True
iteration = 1
result:int
#4.
incorrect_input = True
count_figure:int
figure = ""

#Task 1
for i in range(21):
    if(i%2 == 0):
        sum+=i
print(sum)

#Task 2
print(f"2: {bin(number)}\n 8: {oct(number)}\n 16:{hex(number)}")

#Task 3
while incorrect_time:
    if(current_time - time_before < 0):
        if(time_cycle * iteration + (current_time - time_before) < 0):
            iteration += 1
        else:
            result = time_cycle * iteration + (current_time - time_before)
            incorrect_time = False
    else:
        result = current_time - time_before
        incorrect_time = False
print(f"The time that was {time_before} hours before {current_time}: {result}")

#Task 4
while incorrect_input:
    count_figure = int(input("Count figure: "))
    if(0 < count_figure < 10):
        incorrect_input = False
    else:
        print("Incorrect inputed data")

if(incorrect_input == False):
    figure += "    _~_    " * count_figure + "\n"
    figure += "   (o o)   " * count_figure + "\n"
    figure += "  /  V  \\  " * count_figure + "\n"
    figure += " /(  _  )\\ " * count_figure + "\n"
    figure += "   ^^ ^^   " * count_figure + "\n"
    print(figure)