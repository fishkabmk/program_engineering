random_str = '19814984651384646514684684616874174682145668'


def make_dict(str):
    out_dict = dict()
    for k, v in enumerate(random_str):
        if v in out_dict.keys():
            out_dict[v] += 1
        else:
            out_dict[v] = 1
    print(dict(sorted(out_dict.items())))


make_dict(random_str)