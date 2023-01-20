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


# Task3
def fn(f, n):
    if n < 1:
        return lambda y: y

    return lambda y: fn(f, n - 1)(f(y))


f1 = fn(lambda x: "sin(%s)" % x, 5)
f2 = fn(lambda x: sin(x), 5)
print("%s = %f" % (f1("1"), f2(1)))
print("%s = %f" % (f1("2"), f2(2)))
print(fn(lambda x: sin(x), 0)(1000))


def golden_ratio(n):
    f = fn(lambda x: 1 + (1 / x) if x != 0 else 1, n + 1)
    return f(0)


print(golden_ratio(0))
print(golden_ratio(1))
print(golden_ratio(2))
print(golden_ratio(100))


# Task4
def gen_stream(total, sorted_iterable, extractor=lambda x: x):
    elem_iter = map(extractor, sorted_iterable)
    pos, val = next(elem_iter, (None, None))
    a = 0
    while total is None or a < total:
        if a == pos:
            yield val
            pos, val = next(elem_iter, (None, None))
        else:
            yield 0
        a += 1


precipitation_days = [(3, 1, 4), (5, 2, 6)]


def day_extractor(x):
    months = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    acc = sum(months[:x[1] - 1]) + x[0] - 1
    return acc, x[2]


gen1 = gen_stream(9, [(4, 111), (7, 12)])
print(list(gen1), '\n')
