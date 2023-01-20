from math import sin


# Task1
def to_celsius(temperature_list):
    return list(map(lambda x: (float(5) / 9) * (x - 32), temperature_list))


print(to_celsius([102.56, 97.7, 132.2]))


# Task2
def bold(f):
    def wrapped(*args, **kwargs):
        return "<b>" + f(*args, **kwargs) + "</b>"

    return wrapped


def italic(f):
    def wrapped(*args, **kwargs):
        return "<i>" + f(*args, **kwargs) + "</i>"

    return wrapped


def underline(f):
    def wrapped(*args, **kwargs):
        return "<u>" + f(*args, **kwargs) + "</u>"

    return wrapped


@bold
@italic
@underline
def get_text(name1, name2):
    return "hello " + name1 + " and " + name2


print(get_text(name1="WORLD", name2="SPACE"))
