# 블랙잭
import sys

N, M = map(int, sys.stdin.readline().split())
cardList = list(map(int, sys.stdin.readline().split()))

cardList.sort()

sum = 0
temp = 0
for i in range(0, N):
    if i+1 < N:
        for j in range(i+1, N):
            if j+1 < N:
                for k in range(j+1, N):
                    temp = cardList[i]+cardList[j]+cardList[k]
                    if temp > M:
                        break
                    else:
                        if temp > sum:
                            sum = temp
print(sum)
