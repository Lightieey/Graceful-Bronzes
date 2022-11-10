# 영화감독 숌
import sys

# a_n+1 = 9*a_n + 9*10^(n-2)
# a_1 = 1
# a_2 = 9*1 + 9*10^1 = 18
# a_3 = 9*19 + 9*10 = 261
# a_4 = 9*280 + 9*10*10 =

# 민지코드

N = int(sys.stdin.readline())

nums = [0 for i in range(10000)]

num = 666
i = 0
while i < 10000:
    if str(num).find("666") != -1:
        nums[i] = num
        i += 1
    num += 1

print(nums[N-1])


