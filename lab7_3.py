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
