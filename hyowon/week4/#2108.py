# 통계학
import sys
from collections import Counter

N = int(sys.stdin.readline())

numList = []
sum = 0
for n in range(N):
    num = int(sys.stdin.readline())
    sum += num
    numList.append(num)

#1
avg = round(sum/N)
print(avg)

#2
numList.sort()
print(numList[int(N/2)])

#3
#구글링 코드
countList = Counter(numList).most_common()
if len(countList) == 1:
    print(countList[0][0])
elif countList[0][1] == countList[1][1]:
    print(countList[1][0])
else:
    print(countList[0][0])

#4
print(numList[-1]-numList[0])

# 내 코드
# countList = []
# for n in numList:
#     countList.append(numList.count(n))
#
# if countList.count(max(countList)) > 1:
#
# print(numList[countList.index(max(countList))])

# 다른 사람 시간초과 코드
# sameNoList = list(set(numList)) #중복제거
# maxList = []
# maxCount = 0
# for n in numList:
#     if maxCount == numList.count(n):
#         maxList.append(n)
#     elif maxCount < numList.count(n):
#         maxList = []
#         maxList.append(n)
#         maxCount = numList.count(n)
# if len(maxList) > 1: #최빈값 2개이상
#     maxList.sort()
#     print(maxList[1])
# else: #최빈값 1개
#     print(maxList[0])