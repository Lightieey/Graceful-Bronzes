# 별 찍기 - 2
import sys

N = int(sys.stdin.readline())

for i in range(0, N):
    for j in range(0, N-i):
        print(' ', end='')
    for j in range(N-i-1, N):
        print('*', end='')
    print('')

