# 오븐 시계
import sys

A, B = sys.stdin.readline().split()
C = int(sys.stdin.readline())

C_hour = C // 60
C_min = C % 60


A_end = int(A)+C_hour
B_end = int(B)+C_min

if B_end >= 60:
    A_end += 1
    B_end -= 60

if A_end > 23:
    A_end -= 24

print(A_end, end=' ')
print(B_end)