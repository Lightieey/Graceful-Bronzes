# 패션왕 신해빈
import sys

T = int(input())

case = []
for i in range(T):
    n = int(input())
    costume = dict()
    for j in range(n):
        name, kind = map(str, sys.stdin.readline().split())
        if kind not in costume:
            costume[kind] = [name]
        else:
            costume[kind].append(name)
    case.append(costume)

for c in case:
    mul = 1
    for k in c.keys():
        mul *= len(c[k])+1
    print(mul - 1)
