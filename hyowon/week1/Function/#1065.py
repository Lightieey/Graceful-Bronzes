# 한수
import sys

N = int(sys.stdin.readline())

## 1~99까지는 모두 한수 99
## 세자리 숫자부터 x<=y<=z 성립해야함
## 100의 자리가 1일때(초항이 1일때) -> 111,123,135,147,159 -> 5개

hansoo = 0
if N < 100:
    hansoo = N

elif 100 <= N and N <= 1000:

    count = 0
    for n in range(100, N+1):
        x = n // 100
        y = n // 10 % 10
        z = n % 10

        if x-y == y-z:
            count += 1

    hansoo = 99 + count

print(hansoo)