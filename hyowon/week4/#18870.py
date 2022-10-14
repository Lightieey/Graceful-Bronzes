# 좌표 압축

import sys

N = int(sys.stdin.readline())

x_list = []

x_list = list(map(int, sys.stdin.readline().split()))

sort_list = sorted(list(set(x_list)))

dic = {sort_list[i]: i for i in range(len(sort_list))}
for i in x_list:
    print(dic[i], end=' ')