# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил:
- Трутко Антон Викторович
- ИНО ОЗБ ПОАС-22-2

| Задание    | Сам_раб |
|------------|---------|
| Задание 1  | +       |
| Задание 2  | +       |
| Задание 3  | +       |
| Задание 4  | +       |
| Задание 5  | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Задание:
Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Код:
```python
class Pokemon:
    def __init__(self):
        pass


pokemon = Pokemon()
print(f"Объект типа - {type(pokemon)}")

```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_8/pic/lab8_1.png)

## Самостоятельная работа №2
### Задание:
Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Код:
```python
class Pokemon:
    def __init__(self, name, p_class):
        self.name = name
        self.p_class = p_class

    def use_power(self):
        print(f"{self.name}: Аааааа, ничего не хочу!")


pokemon = Pokemon('Нихачу', 'поддержка')

print(f"Покемон - {pokemon.name}, использует супер силу:")

pokemon.use_power()
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_8/pic/lab8_2.png)

## Самостоятельная работа №3
### Задание:
Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Код:
```python
class Pokemon:
    def __init__(self, name):
        self.name = name

    def use_power(self):
        print(f"{self.name}: Кииия! минус 100хп.")


class PokemonSupport(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.p_class = 'поддержка'

    def heal(self):
        print(f"Лечу 10 хп")


pokemon = PokemonSupport('Нихачу')

print(f"Покемон - {pokemon.name}, класс - {pokemon.p_class}, использует супер силу:")

pokemon.use_power()
pokemon.heal()
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_8/pic/lab8_3.png)

## Самостоятельная работа №4
### Задание:
Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Код:
```python
class Pokemon:
    def __init__(self, name):
        self.name = name

    def use_power(self):
        print(f"{self.name}: Кииия! минус 100хп.")


class PokemonSupport(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.p_class = 'поддержка'
        self.__heal_power = 20

    def heal(self):
        print(f"Лечу {self.__heal_power} хп")


pokemon = PokemonSupport('Нихачу')

print(f"Покемон - {pokemon.name}, класс - {pokemon.p_class}, использует супер силу:")

pokemon.use_power()
pokemon.heal()
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_8/pic/lab8_4.png)

## Самостоятельная работа №5
### Задание:
Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

### Код:
```python
class Pokemon:
    def __init__(self, name):
        self.name = name

    def use_power(self):
        print(f"{self.name}: Кииия! минус 100хп.")


class PokemonSupport(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.p_class = 'поддержка'
        self.__heal_power = 20

    def heal(self):
        print(f"Лечу на {self.__heal_power} хп")

    def use_ability(self):
        print(f"Бафаю на +100 к атаке")


class PokemonWarrior(Pokemon):
    def __init__(self, name):
        super().__init__(name)
        self.p_class = 'воин'
        self.__attack_rating = 90
        self.__attack_damage = 50

    def attack(self):
        print(f"Бью на {self.__attack_damage} хп")

    def use_ability(self):
        print(f"Контратака на {self.__attack_damage * 3} хп")


pokemon = PokemonSupport('Нихачу')
pokemon_war = PokemonWarrior('Лолхачу')

print(f"Покемон - {pokemon.name}, класс - {pokemon.p_class}, использует супервозможность:")

pokemon.heal()
pokemon.use_ability()


print(f"Покемон - {pokemon_war.name}, класс - {pokemon_war.p_class}, использует супервозможность:")

pokemon_war.attack()
pokemon_war.use_ability()
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_8/pic/lab8_5.png)