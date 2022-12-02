#
# #시간초과
# a, b = map(int, input().split())
# #최대공약수
# for i in range(min(a, b)+1, 1, -1): #a, b 중 작은 값부터 1까지 역순으로 for문 진행
#   if (a % i == 0) & (b % i == 0):  #동시에 나눠지면 최대공약수
#     print(i)
#     break
#
# #최소공배수
# for k in range(max(a, b), a*b+1): #a, b 중 큰 값부터 a와 b의 곱까지 진행
#   if (k % a == 0) & (k % b == 0):  #동시에 나눠지면 최소공약수
#     print(k)
#     break

#파이썬 내장함수 사용
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))