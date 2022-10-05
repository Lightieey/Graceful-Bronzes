# 설탕 배달
import math
import sys

N = int(sys.stdin.readline())

minNum = -1

if N % 5 == 0:
    rangeNum = N/5+1
else:
    rangeNum = math.ceil(N/5)

for i in range(0, int(rangeNum)):
    if (N-5*i)%3 == 0:
        j = (N-5*i)/3
        minNum = i+j


print(int(minNum))






