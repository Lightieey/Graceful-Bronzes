# 소수
import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())


# 소수 합 구하기
sum = 0
for x in range(M, N+1):
    # 소수인지 아닌지 판별하는 변수 0: 소수이면 1, 소수아니면 0
    flag = 1

    if x == 1:
        flag = 0
    else:
        for i in range(2, x):
            if x % i == 0:
                flag = 0
                break
    if flag == 1:
        sum += x


# 소수 최솟값
minPrime = 0
# 소수 최솟값 찾기
for x in range(M, N+1):
    # 소수인지 아닌지 판별하는 변수 0: 소수이면 1, 소수아니면 0
    flag = 1

    if x == 1:
        flag = 0
    else:
        for i in range(2, x):
            if x % i == 0:
                flag = 0
                break

    if flag == 1:
        minPrime = x
        break


if sum == 0:
    print(-1)
else:
    print(sum)
    print(minPrime)



## 1 예외처리..꼬옥