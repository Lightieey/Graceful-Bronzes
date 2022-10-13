# 소트인사이드

import sys
N = list(sys.stdin.readline())
'''
# 자리수 세기
count = 0
while N != 0:
    N %= N
    count += 1
'''
del N[-1]
list_a = list(map(int, N))

list_a.sort(reverse=True)

for i in list_a:
    result = ''.join(str(s) for s in list_a)
print(result)