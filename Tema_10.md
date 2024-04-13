# Тема 10. Декораторы и исключения
Отчет по Теме #10 выполнил:
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
Вовочка решил заняться спортивным программированием на python, но для этого он должен знать за какое время выполняется его программа. Он решил, что для этого ему идеально подойдет декоратор для функции, который будет выяснять за какое время выполняется та или иная функция. Помогите Вовочке в его начинаниях и напишите такой декоратор.

### Код:
```python
from time import time


def measure_time(func):
    def wrapper():
        start_time = time()
        result = func()
        end_time = time()
        execution_time =  end_time - start_time
        print(f"\nВремя выполнения функции {func.__name__}: {execution_time} секунд")
        return result
    return wrapper


@measure_time
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end='')


if __name__ == '__main__':
    fibonacci()
    print('\n')
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_10/pic/lab10_1.png)

## Самостоятельная работа №2
### Задание:
Посмотрев на Вовочку, вы также загорелись идеей спортивного программирования, начав тренировки вы узнали, что для решения некоторых задач необходимо считывать данные из файлов. Но через некоторое время вы столкнулись с проблемой что файлы бывают пустыми, и вы не получаете вводные данные для решения задачи. После этого вы решили не просто считывать данные из файла, а всю конструкцию оборачивать в исключения, чтобы избежать такой проблемы. 
Создайте пустой файл и файл, в котором есть какая-то информация. Напишите код программы. Если файл пустой, то, нужно вызвать исключение (“бросить исключение”) и вывести в консоль “файл пустой”, а если он не пустой, то вывести информацию из файла.

### Код:
```python
class EmptyFileError(Exception):
    def __init__(self, message):
        self.message = message


def read_file(file_name):
    with open(file_name, mode="r", encoding="utf-8") as file:
        content = file.readlines()
        if len(content) > 0:
            print(f"Cодержимое файла '{file_name}':")
            for line in content:
                print(line.strip())
        else:
            raise EmptyFileError(f"Файл '{file_name}' пустой\n")


for file in ['lab10_2_text.txt', 'lab10_2_empty.txt']:
    try:
        read_file(file)
    except Exception as e:
        print(e)
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_10/pic/lab10_2.png)

## Самостоятельная работа №3
### Задание:
Напишите функцию, которая будет складывать 2 и введенное пользователем число, но если пользователь введет строку или другой неподходящий тип данных, то в консоль выведется ошибка “Неподходящий тип данных. Ожидалось число.”. Реализовать функционал программы необходимо через try/except и подобрать правильный тип исключения. Создавать собственное исключение нельзя. Проведите несколько тестов, в которых исключение вызывается и нет.

### Код:
```python
def c2():
    try:
        print(2 + int(input("Введите число: ")))

    except ValueError as e:
        print("Неподходящий тип данных. Ожидалось число")


c2()
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_10/pic/lab10_3_1.png)
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_10/pic/lab10_3_2.png)

## Самостоятельная работа №4
### Задание:
Создайте собственный декоратор, который будет использоваться для двух любых вами придуманных функций. Декораторы, которые использовались ранее в работе нельзя воссоздавать.

### Код:
```python
def lowercase_output(func):
    '''
    Декоратор который возвращает вывод функции в нижнем регистре
    '''
    def wrapper():
        result = func()
        return result.lower()
    return wrapper



@lowercase_output
def say_h():
    '''
    Функция которая возвращает строку "Hello World"
    '''
    return "Hello World"


def brrr(func):
    '''
    Функция которая возвращает результат входной функции в обратном портядке
    '''
    result = func
    return result[::-1]


print(brrr(say_h()))
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_10/pic/lab10_4.png)

## Самостоятельная работа №5
### Задание:
Создайте собственное исключение, которое будет использоваться в двух любых фрагментах кода. Исключения, которые использовались ранее в работе нельзя воссоздавать.

### Код:
```python
import re


class NoGreetingError(Exception):
    '''
    Своя ошибка
    '''
    def __init__(self):
        self.message = "В тексте отсутствуют приветственные слова! Вот вам и результат:"


def check(text):
    '''
    Функция которая проверяет текст на наличие приветственных слов
    '''
    pattern = re.compile("Hi|Hello")
    if not re.match(pattern, text):
        raise NoGreetingError
    return text


def text_process(text):
    '''
    Функция которая выводт тест корректно если он прошел проверку на приветственные слова
    '''
    try:
        print(check(text))
    except NoGreetingError as e:
        print(e.message)
        print(text[::-1])


text_process('Bla bla World')
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_10/pic/lab10_5_1.png)
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_10/pic/lab10_5_2.png)