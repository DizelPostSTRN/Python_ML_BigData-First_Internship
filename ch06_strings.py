# Task1
def remove_dots_quotas(text):
    return text.replace('"', '').replace('.', '')


print(remove_dots_quotas('hello..." text'))
