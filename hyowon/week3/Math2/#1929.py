# 소수 구하기
import sys

M, N = map(int, sys.stdin.readline().split())

# 소수 리스트
primeList = []

nonEval = []
for x in range(M, N+1):
    # 소수인지 아닌지 판별하는 변수. 소수이면 1, 소수 아니면 0
    flag = 1
    if x == 1:
        flag = 0
    elif x != 2 and x % 2 == 0:
        flag = 0
    else:
        for i in range(2, x):
            if x % i == 0:
                flag = 0
                break

    if flag == 1:
        primeList.append(x)

for p in primeList:
    print(p)
