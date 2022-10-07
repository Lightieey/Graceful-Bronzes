# 베르트랑 공준
import sys
import math

def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


case_List = []
while True:
    case = int(sys.stdin.readline())
    if case == 0:
        break
    case_List.append(case)

count_List = []
for case in case_List:
    count = 0
    for c in range(case+1, 2*case+1):
        if c%2 == 0 and c != 2:
            continue
        elif isPrime(c):
            count += 1
    count_List.append(count)

for count in count_List:
    print(count)



## 구글링 코드

# def is_prime(n):
#     if n == 2:
#         return True
#
#     if n % 2 == 0:
#         return False
#
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#
#     return True
#
#
# while True:
#     n = int(sys.stdin.readline())
#
#     if n == 0:
#         break
#
#     prime_cnt = 0
#
#     for i in range(n + 1, (2 * n) + 1):
#         if is_prime(i):
#             prime_cnt += 1
#
#     print(prime_cnt)