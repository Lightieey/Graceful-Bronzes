# 단어의 개수
import sys

sentence = sys.stdin.readline().replace('\n', '')

wordList = list(map(str, sentence.split(' ')))
# 공백 개수 카운트
wordNum = [w for w in wordList if w != '']

print(len(wordNum))


## replace(a, b) 특정문자 a를 b로 바꿈
## split(a) a를 기준으로 분할