from lab4_5_2 import calc_triangle


def main():
    a = int(input("Ведите длинну стороны a: "))
    b = int(input("Ведите длинну стороны b: "))
    c = int(input("Ведите длинну стороны c: "))
    calc_triangle(a, b, c)


if __name__ == "__main__":
    main()
