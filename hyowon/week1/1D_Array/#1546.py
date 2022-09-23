# 평균
import sys

N = int(sys.stdin.readline())

cur_score = list(map(int, sys.stdin.readline().split()))

max_score = max(cur_score)
new_sum = 0
for s in cur_score:
    new_sum += s/max_score*100
new_avg = new_sum/N

print(new_avg)