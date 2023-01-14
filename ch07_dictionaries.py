# Task1
def swap_dict(d):
    new_dict = {}
    for k, v in d.items():
        new_dict[v] = new_dict.get(v, tuple()) + (k,)
    return new_dict


print(swap_dict({1: 2, 3: 4, 5: 4, 7: 2, 9: 4}))
