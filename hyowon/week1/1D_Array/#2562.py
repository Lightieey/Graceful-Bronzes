# 최댓값
import sys

N_list = []
for i in range(9):
    N = int(sys.stdin.readline())
    N_list.append(N)

max = N_list[0]
max_index = 0
for n in range(9):
    if N_list[n] >= max:
        max = N_list[n]
        max_index = n+1

print(max)
print(max_index)
