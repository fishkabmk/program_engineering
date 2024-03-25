input = input("Введите предложение на английском: ")
s = input.replace("ugly", "beauty")
print(f"Длинна предложения: {len(s)}")
print(f"Предложение в нижнем регистре: {s.lower()}")
print(f"a: {s.count('a')}, e: {s.count('e')}, i: {s.count('i')}, o: {s.count('o')}, u: {s.count('u')}")
if s.startswith("The") and s.endswith("end"):
    res = "Да"
else:
    res = "Нет"
print(f"Начинается ли предложение на 'The' и заканчивается ли на 'end': {res}")
