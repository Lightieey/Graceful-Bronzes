# 골드바흐의 추측
import sys

T = int(sys.stdin.readline())

even = []
for t in range(T):
    num = int(sys.stdin.readline())
    even.append(num)


# 짝수 = 짝수 + 홀수, 홀수 + 짝수
prime = []
for n in even:
    for i in range(2, n):
        # 2를 제외한 짝수
        if i % 2 == 0 and i != 2:
            break
        else:
            if n % i == 0:
                break
            else:


