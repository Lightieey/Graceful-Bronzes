# 약수
import sys

pNum = int(input())

pList = list(map(int, sys.stdin.readline().split()))

N = max(pList) * min(pList)

print(N)