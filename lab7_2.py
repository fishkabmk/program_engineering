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
