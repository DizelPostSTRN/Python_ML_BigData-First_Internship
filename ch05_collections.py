# Task1
def remove_3_largest(lst):
    res = lst[::-1]
    res.remove(max(res))
    res.remove(max(res))
    res.remove(max(res))
    res.reverse()
    return res


print(remove_3_largest([1, 2, 3, 1, 2, 3]))