# 정수 N개의 합
import sys

def solve(pram):
    return sum(pram)

a = list(map(int, sys.stdin.readline().split()))

print(solve(a))
