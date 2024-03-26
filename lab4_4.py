def calc_avg(*args):
    avg = sum(args) / len(args)
    print(avg)


if __name__ == "__main__":
    calc_avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
