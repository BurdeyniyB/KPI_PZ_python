import string
import time

def choice_type_task() -> int:
    choice: string
    choice = input("Choice count iteration:\n"
                   "1. - recursive method\n"
                   "2. - iterative method\n"
                   "3. - lambda method\n")
    if choice.isdigit() and 0 < int(choice) <= 3:
        return int(choice)
    print("Incorect data!")
    return choice_count_iteration()

def choice_count_iteration() -> int:
    choice: string
    choice = input("Count iteration:\n")
    if choice.isdigit():
        return int(choice)
    print("Incorect data!")
    return choice_count_iteration()

def task(k : int) -> int:
    l: int
    q: int

    q = 1
    for l in range(1, k+1):
        q += (2*l - 1)
    return q

def task_rec(k: int, l: int = 1, q: int = 1) -> int:
    if k == 0:
        return q
    else:
        return task_rec(k - 1, l + 1, q + (2 * l - 1))

task_lambda = lambda k, l=1, q=1: q if k == 0 else task_lambda(k - 1, l + 1, q + (2 * l - 1))


if __name__ == "__main__":
    # Continue program
    continue_program: string
    done = False
    # Data for task
    type_task: int
    count_iteration: int

    # For control spend time
    time_begin: int
    time_after: int
    spend_time: float
    while not done:
        type_task = choice_type_task()
        count_iteration = choice_count_iteration()

        time_begin = time.perf_counter_ns()

        if type_task == 1:
            result = task_rec(count_iteration)
        elif type_task == 2:
            result = task(count_iteration)
        elif type_task == 3:
            result = task_lambda(count_iteration)
        print(f"result: {result}")
        time_after = time.perf_counter_ns()
        spend_time = (time_after - time_begin) / 1000000
        print(f"Time: {spend_time} ms")

        continue_program = input("Do you want to continue? (y/n): ")
        if continue_program.lower() != 'y':
            done = True
