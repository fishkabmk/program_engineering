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
