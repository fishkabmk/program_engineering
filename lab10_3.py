def c2():
    try:
        print(2 + int(input("Введите число: ")))

    except ValueError as e:
        print("Неподходящий тип данных. Ожидалось число")


c2()
