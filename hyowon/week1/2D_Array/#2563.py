# 색종이
import sys

PAPER = [[0 for w in range(100)] for h in range(100)]

N = int(sys.stdin.readline())

xy_list = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xy_list.append([x, y])

    for h in range(99-(y+10), 99-y):
        for w in range(x, x+10):
            PAPER[h][w] += 1

sum = 0
for h in range(100):
    for w in range(100):
        if PAPER[h][w] >= 1:
            sum += 1

print(sum)
