# 이항 계수1
import sys

N, K = map(int, sys.stdin.readline().split())

mul = 1
div = 1
result = 0
for i in range(K):
    mul *= N-i
    div *= K-i
    result = mul/div

if K == 0:
    result = 1

print(int(result))