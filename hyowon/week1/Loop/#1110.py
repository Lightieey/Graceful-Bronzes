# 더하기 사이클

import sys

N = int(input('정수 입력: '))

origin = N
N_new = -1
count = 0

while True:
    if 0 <= N and N < 10:
        N_new = N * 10 + N

    elif 10 <= N and N < 100:
        N_left = N // 10
        N_right = N % 10
        N_lr_sum = N_left + N_right
        N_new = N_right * 10 + N_lr_sum % 10

    count += 1
    if origin == N_new:
        break
    else:
        N = N_new

print(count)