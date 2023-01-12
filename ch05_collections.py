# Task1
def remove_3_largest(lst):
    res = lst[::-1]
    res.remove(max(res))
    res.remove(max(res))
    res.remove(max(res))
    res.reverse()
    return res


print(remove_3_largest([1, 2, 3, 1, 2, 3]))


# Task2
def get_unique_lists_num(one, two, tree, four):
    return len(set(map(tuple, (one, two, tree, four))))


one = [1, 2, 3]
two = [1, 2, 3]
tree = [3, 4, 5]
four = [3, 2, 1]
print(get_unique_lists_num(one, two, tree, four))


# Task3
def get_max_common(a, b):
    return max(set(a) & set(b) | {0})


a = [1, 2, 3, 4, 5]
b = [0, 1, 3, 5, 7]
print(get_max_common(a, b))
