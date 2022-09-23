# 최소, 최대
import sys

N = int(input())

N_list = list(map(int, sys.stdin.readline().split()))

min = N_list[0]
max = N_list[0]

for i in N_list:
    if i < min:
        min = i
    if i > max:
        max = i

print(min, end=' ')
print(max)
