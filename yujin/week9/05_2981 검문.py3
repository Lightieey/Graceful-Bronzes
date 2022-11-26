from math import gcd
from math import sqrt

N = int(input())
num_list = []
for i in range(N):
  num_list.append(int(input()))
num_list.sort(reverse=True)

sub_list=[]
for i in range(1,N):
  sub_list.append(num_list[i-1] - num_list[i])

prev = sub_list[0]
for i in range(1, len(sub_list)):
    prev = gcd(prev, sub_list[i])
yasksu = []
for i in range(2, int(sqrt(prev)) + 1): #제곱근까지만 탐색
    if prev % i == 0:
        yasksu.append(i)
        yasksu.append(prev//i)
yasksu.append(prev)
yasksu = list(set(yasksu)) #중복이 있을수 있으니 제거
yasksu.sort()
print(*yasksu)