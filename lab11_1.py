def fib(count):
    a, b = 1, 1
    for f in range(1, count):
        a, b = b, a + b
        yield a


counter = 0
for i in fib(210):
    counter += 1
    if counter > 200:
        print(i)
