# 그룹 단어 체커

import sys

N = int(input())

# [aba, abab, abcabc, a]
wordList = []
for i in range(N):
    word = sys.stdin.readline()
    wordList.append(word)


count = 0 # 그룹 단어가 아닌 개수
existWord = []  # 그룹 단어 체크를 위한 문자 리스트
# [a, b]
# [a, b]
# [a, b, c]


for word in wordList:
    for i in range(len(word)-1):
        if i == 0:
            existWord.append(word[i])
        else:
            if word[i] not in existWord:
                existWord.append(word[i])
            else:
                if word[i] != word[i-1]:
                    count += 1
                    existWord.clear()
                    break
    existWord.clear()

print(len(wordList) - count)






