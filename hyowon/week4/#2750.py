# 수 정렬하기
import sys

def sort(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]

N = int(sys.stdin.readline())

numList = []
for i in range(N):
    numList.append(int(sys.stdin.readline()))

sort(numList)

for n in numList:
    print(n)