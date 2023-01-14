# Task1
def swap_dict(d):
    new_dict = {}
    for k, v in d.items():
        new_dict[v] = new_dict.get(v, tuple()) + (k,)
    return new_dict


print(swap_dict({1: 2, 3: 4, 5: 4, 7: 2, 9: 4}))


# Task2
def compact_dict(d):
    new_dict = swap_dict(d)
    return {v: k for k, v in new_dict.items()}


print(compact_dict({1: 2, 3: 4, 5: 4, 7: 2, 9: 4}))
