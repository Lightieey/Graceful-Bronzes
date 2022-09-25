import sys
n = int(sys.stdin.readline())
n_list = list(map(int, input().split()))
print(min(n_list), max(n_list))