counter = 0
values = [0 ,2 ,4, 6, 8, 10]
while counter != 10:
    string = 'hello'
    while ' world' not in string:
        memory = ' world'
        if counter in values:
            print(string + memory)
            print(string)
        string = string + ' world'
        memory = string
        string = ' world'
    counter += 1
print(memory)
