# 통계학
import sys

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
numList.sort(reverse=True)
print(numList[N//2])

#3
countList = []
for n in numList:
    countList.append(numList.count(n))

print(numList[countList.index(max(countList))])


#4
print(numList[0]-numList[-1])

