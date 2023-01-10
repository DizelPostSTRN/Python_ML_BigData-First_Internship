import math


# Task 1
def get_day_week(day, starting_dotw):
    return (starting_dotw + day - 2) % 7 + 1


print(get_day_week(7, 3))


# Task 2
def count_digits(n):
    return int(math.log10(n))+1


print(count_digits(12345678))