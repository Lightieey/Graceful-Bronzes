# 다리 놓기
import sys

T = int(input())

case = []
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())

    mul = 1
    div = 1
    for i in range(N):
        mul *= M - i
        div *= N - i
        result = mul / div

    case.append(int(result))

for c in case:
    print(c)