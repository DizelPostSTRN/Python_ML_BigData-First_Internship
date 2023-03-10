# Task1
def remove_dots_quotas(text):
    return text.replace('"', '').replace('.', '')


print(remove_dots_quotas('hello..." text'))


# Task2
def borded_string(s):
    return "{2:{2}^{1}}\n{2} {0} {2}\n{2:{2}^{1}}".format(s, len(s) + 4, "#")


print(borded_string('Armando'))


# Task3
def unborded_string(s):
    return s.split('\n')[1][1: -1]


print(unborded_string(borded_string('Armando')))


# Task4
def normalize_name(s):
    return ' '.join(s.title().split())


print(normalize_name('сэр Артур Конан Дойл'))
