counter = 0
values = [0 ,2 ,4, 6, 8, 10]
while counter != 10:
    string = 'hello'
    while ' world' not in string:
        memory = ' world'
        if counter in values:
            print(string + memory)
            print(string)
        string = ' world'
    if counter > 7:
        string = 'hello'
    counter += 1
string = string + ' world'
print(string)
