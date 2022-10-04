# 분수찾기
import math

# 규칙
# 1. 순서가 n줄에 위치할 때, 분모 최대 숫자는 n이다.
# 2. 분모 최대 숫자가 n일 때, N번째 수의 x는 (n-1)n/2 < N <= n(n+1)/2이다.
# 3. n이 짝수일 때는, 분모가 감소하고, 홀수일 때는 분모가 증가한다.
# 4. 분모와 분자의 합은 n+1이다.

import sys

N = int(sys.stdin.readline())

# n줄 찾기 -> n**2+n-2N=0의 근의 공식 해
n = math.ceil((-1+(1+8*N)**(1/2))/2)

# n줄에서 몇 번째인지 확인
k = N - (n-1)*n/2


# n 짝수인지, 홀수인지에 따라 분수 출력
if n % 2 == 0:
    print(str(int(k))+"/"+str(int(n+1-k)))
else:
    print(str(int(n+1-k))+"/"+str(int(k)))




