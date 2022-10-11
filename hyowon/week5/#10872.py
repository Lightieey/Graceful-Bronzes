# 팩토리얼
import sys

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num*factorial(num-1)

N = int(sys.stdin.readline())

print(factorial(N))