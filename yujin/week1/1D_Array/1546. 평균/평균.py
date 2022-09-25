import sys
N = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))
M = max(score_list)
s = 0
for i in range(0, N):
  s+= score_list[i]/M*100
print(s/N)