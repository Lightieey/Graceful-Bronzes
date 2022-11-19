#counter 함수 사용
from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
for i in range(len(M)):
    if M[i] in C:
        print(C[M[i]], end=' ')
    else:
        print(0, end=' ')



# import sys
# N = int(sys.stdin.readline().strip())
# sang_list=list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline().strip())
# num_set = list(map(int, sys.stdin.readline().split()))
# for num in num_set:
#   print(sang_list.count(num), end=" ")