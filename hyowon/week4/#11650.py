# 좌표정렬하기

import sys

N = int(sys.stdin.readline())

list_xy = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    list_xy.append([x, y])

list_xy.sort()

for i in list_xy:
    print(' '.join(str(s) for s in i))