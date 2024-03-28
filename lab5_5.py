list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def make_set(list_in):
    counter = {}
    for l in list_in:
        counter[l] = list_in.count(l)

    newset = set()
    for c in counter:
        if counter[c] >= 1:
            newset.add(c)
        if counter[c] >= 2:
            for m in range(2, counter[c] + 1):
                newset.add(str(c) * m)
    print(newset)


make_set(list_1)
make_set(list_2)
make_set(list_3)
