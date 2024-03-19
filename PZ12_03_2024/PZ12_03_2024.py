#-------------Practice Lesson 5------------
import string
import math
from datetime import datetime

def write_sequence_to_file(sequence, filename) -> None:
    with open(filename, 'w') as file:
        for item in sequence:
            file.write("%s\n" % item)

def read_sequence_from_file(filename) -> [string]:
    with open(filename, 'r') as file:
        sequence = file.readlines()
        sequence = [item.strip() for item in sequence]
        return sequence

def calculate_distance(lat1, lon1, lat2, lon2) -> float:
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    earth_radius = 6371.032

    distance = earth_radius * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

    return distance

def is_valid_date(date_str):
    date_parts = date_str.split()
    if len(date_parts) != 3:
        return False
    for part in date_parts:
        if not part.isdigit():
            return False
    return True

def is_valid_time(time_str):
    time_parts = time_str.split(":")
    if len(time_parts) != 3:
        return False
    for part in time_parts:
        if not part.isdigit():
            return False
    return True

if __name__ == "__main__":
    #Variables for tasks
    #1.
    input_sequence = ['Python', 'Ruby', 'C++', 'C', 'Java', 'Go', 'JavaScript']
    input_filename = 'input.txt'
    output_sequence: [string]
    #2.
    lat1 = 39.9075000
    lon1 = 116.3972300
    lat2 = 50.4546600
    lon2 = 30.5238000
    distance: float
    #3.
    date_str: string
    time_str: string

    #Task 1
    write_sequence_to_file(input_sequence, input_filename)
    output_sequence = read_sequence_from_file(input_filename)

    for item in output_sequence:
        print(item)

    #Task 2
    distance = calculate_distance(lat1, lon1, lat2, lon2)

    print("The distance is {:.2f} km.".format(distance))

    #Task 3
    date_str = input("Введіть рік, місяць та день у форматі 'Рік Місяць День': ")
    while not is_valid_date(date_str):
        print("Некоректний формат. Повторіть введення.")
        date_str = input("Введіть рік, місяць та день у форматі 'Рік Місяць День': ")
    date_obj = datetime.strptime(date_str, "%Y %m %d")

    time_str = input("Введіть години, хвилини та секунди у форматі 'Години Хвилини Секунди': ")
    while not is_valid_time(time_str):
        print("Некоректний формат. Повторіть введення.")
        time_str = input("Введіть години, хвилини та секунди у форматі 'Години Хвилини Секунди': ")
    time_obj = datetime.strptime(time_str, "%H:%M:%S")

    current_datetime = datetime.now()

    time_difference = current_datetime - datetime.combine(date_obj.date(), time_obj.time())

    print(
        f"{time_difference.days} days, {time_difference.seconds // 3600} hours, {(time_difference.seconds // 60) % 60} minutes, {time_difference.seconds % 60} seconds")