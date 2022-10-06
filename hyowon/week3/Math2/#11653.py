# 소인수분해
import sys

# 소수의 곱으로 나타내기?

N = int(sys.stdin.readline())

while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            print(i)
            N = N // i
            break


