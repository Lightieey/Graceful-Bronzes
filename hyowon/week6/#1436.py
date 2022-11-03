# 영화감독 숌
import sys

# a_n+1 = 9*a_n + 9*10^(n-2)
# a_1 = 1
# a_2 = 9*1 + 9*10^1 = 18
# a_3 = 9*19 + 9*10 = 261
# a_4 = 9*280 + 9*10*10 =

list = [666, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668, 6669, 7666, 8666, 9666]

N = int(sys.stdin.readline().split())

i = 1
a_cur = 1
a_sum = 0
a_pre = 0
while True:
    if N <= a_sum:
        temp = N - a_sum
        if temp <= a_pre*5:
            for j in range(1, 6):
                t = temp - a_pre*j
                if t < 0:
                    break

        # elif a_pre*5 < temp <= a_pre*5 + 9*(10**(i-1)):
        #
        # else:
        #
        # r = temp % a_pre


    else:
        a_sum += a_cur
        a_pre, a_cur = a_cur, a_sum*9 + 9*(10**i)
        i += 1

