# 직각삼각형
import sys

test_case = []
while True:
    x, y, z = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0 and z == 0:
        break
    test_case.append([x, y, z])

for t in test_case:
    if t[0] >= t[1] and t[0] >= t[2]:
        if t[0]**2 == t[1]**2 + t[2]**2:
            print("right")
        else:
            print("wrong")
    elif t[1] >= t[2] and t[1] >= t[0]:
        if t[1] ** 2 == t[0] ** 2 + t[2] ** 2:
            print("right")
        else:
            print("wrong")
    elif t[2] >= t[0] and t[2] >= t[1]:
        if t[2] ** 2 == t[0] ** 2 + t[1] ** 2:
            print("right")
        else:
            print("wrong")
