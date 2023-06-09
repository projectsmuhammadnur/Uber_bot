import random

def randomize_numbers(start, end):
    numbers = list(range(start, end + 1))
    random.shuffle(numbers)
    return numbers

start_number = 99999
end_number = 999999

random_numbers = randomize_numbers(start_number, end_number)
print(random_numbers)