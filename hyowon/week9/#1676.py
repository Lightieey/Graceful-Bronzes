# 팩토리얼 0의 개수

N = int(input())

mul = 1
for i in range(1, N+1):
    mul *= i

str_mul = str(mul)
zero_count = 0
while str_mul[-1] == '0':
    zero_count += 1
    str_mul = str_mul[0:-1]

print(zero_count)