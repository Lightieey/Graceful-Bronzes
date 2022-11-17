# 대칭 차집합
import sys

A_n, B_n = map(int, sys.stdin.readline().split())

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

A_B = A.difference(B)
B_A = B.difference(A)

print(len(A_B) + len(B_A))