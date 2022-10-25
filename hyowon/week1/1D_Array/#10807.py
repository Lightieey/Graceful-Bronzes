# 개수 세기
import sys

# 형식
N = int(sys.stdin.readline())

N_List = list(map(int, sys.stdin.readline().split()))

v = int(sys.stdin.readline())

count = 0
for n in N_List:
    if n == v:
        count += 1

print(count)