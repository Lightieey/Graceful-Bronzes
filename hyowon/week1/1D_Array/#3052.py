# 나머지

import sys

N_remain = []
for i in range(10):
    N = int(sys.stdin.readline())
    N_remain.append(N%42)

N_uniq = []
for n in N_remain:
    if n not in N_uniq:
        N_uniq.append(n)

print(len(N_uniq))


## 리스트 안에 포함 여부 not in, in
