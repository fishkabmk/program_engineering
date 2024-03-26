from random import randrange


def roll():
    roll_result = randrange(1, 7)
    print(f"Результат броска: {roll_result}")
    if roll_result in [5, 6]:
        print(f"Вы победили")
    elif roll_result in [1, 2]:
        print(f"Вы проиграли")
    else:
        roll()


if __name__ == "__main__":
    roll()
