# 덩치
import sys

N = int(sys.stdin.readline())

people_body = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    people_body.append((x, y))

rank = 1
for i in range(N):
    for j in range(N):
        if people_body[i][0] < people_body[j][0]:
            if people_body[i][1] < people_body[j][1]:
                rank += 1
    print(rank, end=' ')
    rank = 1
