# Task 1
def get_day_week(day, starting_dotw):
    return (starting_dotw + day - 2) % 7 + 1


print(get_day_week(7, 3))
