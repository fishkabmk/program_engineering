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
