# 소수 찾기

# 소수인지 아닌지 판별하는 법.. 구글링ㅎㅎ
# X를 2부터 X-1까지의 모든 수로 나누어 떨어지면 소수 아님

import sys

N = int(sys.stdin.readline())

num_List = list(map(int, sys.stdin.readline().split()))

count = 0

for n in num_List:
    if n > 1:
        for j in range(2, n):
            if n % j == 0:
                count += 1
                break
    else:
        count += 1

print(N - count)