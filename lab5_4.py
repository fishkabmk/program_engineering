l1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
l2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
l3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]


def make_good(l_in):
    ll = [i for i in l_in if i != 2]
    for i in range(len(ll)):
        if ll[i] == 3:
            ll[i] = 4
    print(ll)


make_good(l1)
make_good(l2)
make_good(l3)
