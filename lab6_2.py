in_1 = (1, 2, 3) # 1
in_2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2) # 3
in_3 = (2, 4, 6, 6, 4, 2) # 9


def remove_digit(digit, in_tuple):
    if digit in in_tuple:
        li = list(in_tuple)
        li.remove(digit)
        return tuple(li)
    else:
        return in_tuple


print(remove_digit(1, in_1))
print(remove_digit(3, in_2))
print(remove_digit(9, in_3))