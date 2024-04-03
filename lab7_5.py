'''
Имеется файл с тексом.
Нужно найти самые длинные слова в тексте
'''

def longest_words(file):
    with open(file, encoding='utf-8') as text:
        content = text.read()
        print(content)
        words = content.split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(f"Самые длинные слова в тексте: {longest_words('words.txt')}")
