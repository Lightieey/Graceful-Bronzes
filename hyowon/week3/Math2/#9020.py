# 골드바흐의 추측
import sys

## 시간 초과난 코드
def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

T = int(sys.stdin.readline())

numList = []
for t in range(T):
    num = int(sys.stdin.readline())
    numList.append(num)


# 소수+소수 = 짝수 = 홀수+홀수, 짝수+짝수(2일때만)
for num in numList:
    one, two = 0, 0
    for i in range(2, num//2+1):
        # 2가 아닌 짝수는 소수 아님 => 빨리 다음 i 수행
        if i % 2 == 0 and i != 2:
            continue
        # 소수인 경우
        elif isPrime(i) and isPrime(num-i):
            one, two = i, num-i
        # 소수가 아닌 경우
        else:
            continue
    print(one, two)


# 구글링 코드

# 핵심 키
# 입력 받은 값 N의 중간 지점부터 접근을 해서
# 가장 가까운 소수를 찾아가는 방식으로 풀어야합니다.

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1