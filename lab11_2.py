def fib(count):
    a, b = 1, 1
    for f in range(1, count):
        a, b = b, a + b
        yield a


def wire_file(num):
    with open("fib.txt", mode="a", encoding="utf-8") as file:
        file.write(str(num) + "\n")


counter = 0
for i in fib(210):
    wire_file(i)
    counter += 1
    if counter > 200:
        print(i)
