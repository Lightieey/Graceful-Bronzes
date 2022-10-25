# 행렬 덧셈
import sys

N, M = map(int, sys.stdin.readline().split())

A = []
B = []

for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

result = []
for i in range(N):
    list = []
    for j in range(M):
        list.append(A[i][j] + B[i][j])
    result.append(list)

for i in range(N):
    for j in range(M):
        print(result[i][j], end=' ')
    print('')
