in_1 = (1, 2, 3)  # 8
in_2 = (1, 8, 3, 4, 8, 8, 9, 2)  # 8
in_3 = (1, 2, 8, 5, 1, 2, 9)  # 8


def func(id, in_tuple):
    indexes = [i for i in range(len(in_tuple)) if in_tuple[i] == id]
    if len(indexes) == 0:
        print(tuple())
    if len(indexes) == 1:
        print(in_tuple[indexes[0]:])
    if len(indexes) >= 2:
        print(in_tuple[indexes[0]:indexes[1+1]])


func(8, in_1)
func(8, in_2)
func(8, in_3)
