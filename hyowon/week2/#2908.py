# 상수
import sys

A, B = map(str, sys.stdin.readline().split())

ANum = []
BNum = []
for i in range(3):
    ANum.append(A[i])
    BNum.append(B[i])

ANum[0], ANum[2] = ANum[2], ANum[0]
BNum[0], BNum[2] = BNum[2], BNum[0]

A_new = ""
B_new = ""
for i in range(3):
    A_new += ANum[i]
    B_new += BNum[i]

if int(A_new) > int(B_new):
    print(A_new)
else:
    print(B_new)