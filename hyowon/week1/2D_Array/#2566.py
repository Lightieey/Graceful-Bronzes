# 최댓값
import sys

matrix = []
for i in range(9):
    matrix.append(list(map(int, sys.stdin.readline().split())))

real_max = 0
idx = 1
jdx = 1
for i in range(9):
    list_max = max(matrix[i])
    if real_max < list_max:
        real_max = list_max
        jdx = matrix[i].index(list_max) + 1
        idx = i + 1

print(real_max)
print(idx, jdx)

