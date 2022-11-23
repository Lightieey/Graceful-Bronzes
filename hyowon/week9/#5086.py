# 배수와 약수
import sys

N = -1
M = -1

answer = []

while N != 0 and M != 0:
    N, M = map(int, sys.stdin.readline().split())
    if N > 0 and M > 0:
        if M % N == 0:
            answer.append('factor')
        elif N % M == 0:
            answer.append('multiple')
        else:
            answer.append('neither')

print('\n'.join(str(a) for a in answer))