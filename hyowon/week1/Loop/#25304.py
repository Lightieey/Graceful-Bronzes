# 영수증
import sys

X = int(input())
N = int(input())

total = 0
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    total += a*b

if total == X:
    print("Yes")
else:
    print("No")