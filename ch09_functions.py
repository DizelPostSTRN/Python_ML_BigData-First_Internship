from math import sin


# Task1
def to_celsius(temperature_list):
    return list(map(lambda x: (float(5) / 9) * (x - 32), temperature_list))


print(to_celsius([102.56, 97.7, 132.2]))