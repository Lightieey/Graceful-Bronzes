# 손익분기점
import math
import sys

A, B, C = map(int, sys.stdin.readline().split())

# N은 판매량
if C > B:
    N = math.ceil(A/(C-B)+1)
else:
    N = -1

print(N)
