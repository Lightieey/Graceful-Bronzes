# 골드바흐의 추측
import sys
# t
def isPrime(num):
    if num == 2:
        return True
    else:
        for i in range(2, num):
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
    one = 0
    two = 0
    for i in range(2, num):
        # 2가 아닌 짝수는 소수 아님 => 빨리 다음 i 수행
        if i % 2 == 0 and i != 2:
            continue
        # 소수인 경우
        elif isPrime(i):
            if isPrime(num-i):
                if i <= num-i:
                    one = i
                    two = num-i
        # 소수가 아닌 경우
        else:
            continue
    print(one, end=' ')
    print(two)


