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