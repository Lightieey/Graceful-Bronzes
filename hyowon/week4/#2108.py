# 통계학
import sys

N = int(sys.stdin.readline())

numList = []
sameNoList = []
sum = 0
for n in range(N):
    num = int(sys.stdin.readline())
    sum += num
    numList.append(num)
    if n not in sameNoList:
        sameNoList.append(n)

#1
avg = sum/N
print(avg)

#2
numList.sort()
print(numList[N//2])

#3
sameNoList.sort()
countList = [0]*len(sameNoList)
for i in range(0, N):
    countList[i] += 1
    if i > 0:
        if sameNoList[i] == sameNoList[i-1]:
            countList[i-1] += 1
        else:
            countList[i] += 1

print(sameNoList[countList.index(max(countList))])

#4
print(numList[-1]-numList[0])

