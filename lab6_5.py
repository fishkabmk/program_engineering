'''
Игра в лотерею
Сгенерируем 30 цифр от 1 до 90 случайнм образом
Игрок вводит 3 цифры через запятую, проверяем, еслить ли совпадения введенных цифр со списком лотерейных цифр
'''
import random
loto = [random.randint(1, 90) for x in range(30)]

user_input = input("Введите номера от 1 до 90 через запятую: ")
user_tuple = tuple(int(x) for x in user_input.split(","))

print(f"Номера лотерии: {loto}")
for item in user_tuple:
    if item in loto:
        print(f"Вы выйграли с номером: {item}")
