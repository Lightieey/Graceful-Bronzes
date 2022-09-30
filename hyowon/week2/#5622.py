# 다이얼
import sys

alphabet = sys.stdin.readline()

dial = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# 알파벳 리스트
alphabetList = []
for i in range(len(alphabet)-1):
    alphabetList.append(alphabet[i])

# 알파벳에 따른 번호 찾기
numberList = []
for i in alphabetList:
    for j in dial:
        if i in j:
            numberList.append(dial.index(j))

# print(alphabetList)
# print(numberList)

# 걸린 시간 구하기
# 1은 2초, 2는 3초, ..., 9는 10초, 0은 11초
time = 0
for n in numberList:
    if n != 0:
        time += n+1
    else:
        time += 11

print(time)

