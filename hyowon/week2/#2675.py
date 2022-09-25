# 문자열 반복
import sys

T = int(sys.stdin.readline())

S_list = []
R_list = []
for i in range(T):
    S, R = map(str, sys.stdin.readline().split())
    S_list.append(int(S))
    R_list.append(R)

for i in range(T):
    for r in R_list[i]:
        print(r * S_list[i], end='')
    print('')


