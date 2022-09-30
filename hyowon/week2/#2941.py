# 크로아티아 알파벳

# 문자열에서 특정문자열 제거방법
# strip(regex) replace(regex, ''), sub(regex, '', str)
# strip은 양 끝단의 문자열만 삭제할 수 있다.
# count 문자열에서 특정 문자열 개수 세는 데 사용
import sys

word = sys.stdin.readline()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


# 크로아티아 알파벳 분리
alphabet = []
for c in croatia:
    if c in word:
        for i in range(word.count(c)):
            alphabet.append(c)
        word = word.replace(c, ' ')


# 나머지 알파벳 분리
for w in word:
    if w != '\n' and w != ' ':
        alphabet.append(w)

print(len(alphabet))



