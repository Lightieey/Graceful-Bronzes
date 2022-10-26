# 대표값2
import sys

N_list = []
sum = 0
for i in range(5):
    num = int(sys.stdin.readline())
    N_list.append(num)
    sum += num

avg = int(sum / 5)

N_list.sort()

print(avg)
print(N_list[2])
