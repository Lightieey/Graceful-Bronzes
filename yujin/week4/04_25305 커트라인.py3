import sys
N, k = map(int, sys.stdin.readline().split())
score_list = list(map(int, sys.stdin.readline().split()))
score_list.sort(reverse=True) # 내림차순
print(score_list[k-1])