# 크로아티아 알파벳

# 문자열에서 특정문자열 제거방법
# strip(regex) replace(regex, ''), sub(regex, '', str)

import sys

word = sys.stdin.readline()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


# 크로아티아 알파벳 분리
alphabet = []
for c in croatia:
    if c in word:
        alphabet.append(c)
        word = word.strip(c)
        # new_word = word.strip(c)
        # word, new_word = new_word, word
        print(word)


# 나머지 알파벳 분리
for w in word:
    alphabet.append(w)

print(alphabet)



