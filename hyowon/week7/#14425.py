# 문자열 집합
import sys

N, M = map(int, sys.stdin.readline().split())

N_list = []
M_list = []

for i in range(N):
    N_list.append(sys.stdin.readline())

N_list = set(N_list)
count = 0
for i in range(M):
    M_list.append(sys.stdin.readline())
    if M_list[i] in N_list:
        count += 1

print(count)
