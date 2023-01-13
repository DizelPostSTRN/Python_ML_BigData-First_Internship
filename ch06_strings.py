# Task1
def remove_dots_quotas(text):
    return text.replace('"', '').replace('.', '')


print(remove_dots_quotas('hello..." text'))


# Task2
def borded_string(s):
    return "{2:{2}^{1}}\n{2} {0} {2}\n{2:{2}^{1}}".format(s, len(s) + 4, "#")


print(borded_string('Armando'))
