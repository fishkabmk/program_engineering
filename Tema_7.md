# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил:
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
Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

### Код:
```python
from collections import Counter
import re

words = []
with open('text.txt', encoding='utf-8', mode='r') as file:
    for line in file:
        chunks = line.strip().split(' ')
        word = re.compile('[а-я]+', re.IGNORECASE)
        for chunk in chunks:
            if word.match(chunk):
                words.append(chunk)

print(f"Слов в статье: {len(words)}")
c = Counter(words)
most_common_key = c.most_common(1)[0][0] if c else None
print(f"В статье чаще всего встречается слово - '{most_common_key}', количество повторений - '{c[most_common_key]}'")
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_7/pic/lab7_1_f.png)
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_7/pic/lab7_1.png)

## Самостоятельная работа №2
### Задание:
У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

### Код:
```python
with open('book.txt', mode='a+', encoding='utf-8') as file:
    cur_pos = file.tell()
    file.seek(0)
    content = []
    for line in file:
        content.append(line)
    new_line = input("Введите информацию о расходах: ")
    content.append(new_line)
    file.seek(cur_pos)
    file.writelines(new_line + "\n")
    print(content)
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_7/pic/lab7_2_f.png)
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_7/pic/lab7_2.png)

## Самостоятельная работа №3
### Задание:
Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.  
Текст в файле:  
Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.

### Код:
```python
with open('input.txt', mode='r', encoding='utf-8') as file:
    letters = []
    words = []
    lines = 0
    for line in file:
        lines += 1
        letters += line.replace('\n', '').replace('.', '').replace(' ', '').strip()
        words += line.split(' ')


print(f"{len(letters)} letters")
print(f"{len(words)} words")
print(f"{lines} lines")
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_7/pic/lab7_3.png)

## Самостоятельная работа №4
### Задание:
Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова.   
Замена производится независимо от регистра:   
если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

### Код:
```python
import re

test_str = "Hello, world! Python IS the programming language of thE future. My EMAIL is... \n" \
           "PYTHON is awesome!!!!"


def censor(text, word):
    t = str(text)
    w = str(word)
    if w in t.lower():
        l = len(w)
        item = ("*" * l)
        pattern = re.compile(word, re.IGNORECASE)
        return pattern.sub(item, t)
    else:
        return t


censored_text = test_str
with open('input_4.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        for word in line.split(' '):
            censored_text = censor(censored_text, word)

print(censored_text)
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_7/pic/lab7_4.png)

## Самостоятельная работа №5
### Задание:
Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

### Код:
```python
'''
Имеется файл с тексом.
Нужно найти самые длинные слова в тексте
'''

def longest_words(file):
    with open(file, encoding='utf-8') as text:
        content = text.read()
        print(content)
        words = content.split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(f"Самые длинные слова в тексте: {longest_words('words.txt')}")
```
### Результат:
![img](https://github.com/fishkabmk/program_engineering/blob/Тема_7/pic/lab7_5.png)