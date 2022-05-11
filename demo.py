
def count_integer(list1):
    f_list = list(map(lambda i: isinstance(i, float), list1))
    result = len([i for i in f_list if i])
    return result


mixed_list = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(count_integer(mixed_list))