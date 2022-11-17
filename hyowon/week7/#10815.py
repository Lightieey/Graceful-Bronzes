# 숫자 카드
import sys

N = sys.stdin.readline()
N_card = list(map(int, sys.stdin.readline().split()))

M = sys.stdin.readline()
M_card = list(map(int, sys.stdin.readline().split()))

N_card = set(N_card)

for m in M_card:
    if m in N_card:
        print(1, end=' ')
    else:
        print(0, end=' ')
