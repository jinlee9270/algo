from functools import cmp_to_key
n = int(input())
words = []


def comparer(a, b):
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1
    else:
        if a > b:
            return 1
        else:
            return -1


for i in range(0, n):
    words.append(input())
words_set = set(words)
new_words = list(words_set)

final_words = sorted(new_words, key=cmp_to_key(comparer))

for i in range(0, len(new_words)):
    print(final_words[i])
    
