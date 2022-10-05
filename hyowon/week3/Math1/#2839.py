# 설탕 배달
import math
import sys

N = int(sys.stdin.readline())

minNum = -1
tfNum = -1
# 5로 나누어 떨어지면 최소 개수는 5로 나누었을 때
if N % 5 == 0:
    minNum = N / 5
# 3으로 나누어 떨어지면 최대 개수는 3으로 나누었을 때
# elif N % 3 == 0:
#     minNum = N / 3
#     tfNum = minNum

for i in range(0, math.ceil(N/3)):
    if (N-3*i)%5 == 0:
        j = (N-3*i)/5
        tfNum = i+j
    if minNum > tfNum or (minNum == -1 and tfNum != -1):
        minNum = tfNum


print(int(minNum))






