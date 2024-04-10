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
