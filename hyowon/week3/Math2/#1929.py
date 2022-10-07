# 소수 구하기

## 내 시간 초과한 코드
import sys
def isPrime(num):
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

M, N = map(int, sys.stdin.readline().split())

for x in range(M, N+1):
    if x == 1:
        continue
    elif x != 2 and x % 2 == 0:
        continue
    else:
        if isPrime(x):
            print(x)


## 구글링 코드

# 핵심 키
# 특정 수의 제곱근을 구해, 그 제곱근까지의 약수를 구하면
# 해당 약수를 포함하는 수를 모두 제거할 수 있다

m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1: #1은 소수가 아니므로 제외
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)