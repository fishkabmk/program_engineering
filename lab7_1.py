from collections import Counter
import re

words = []
with open('text.txt', encoding='utf-8', mode='r') as file:
    for line in file:
        chunks = line.strip().split(' ')
        word = re.compile('[а-я]+', re.IGNORECASE)
        for chunk in chunks:
            if word.match(chunk):
                words.append(chunk)

print(f"Слов в статье: {len(words)}")
c = Counter(words)
most_common_key = c.most_common(1)[0][0] if c else None
print(f"В статье чаще всего встречается слово - '{most_common_key}', количество повторений - '{c[most_common_key]}'")