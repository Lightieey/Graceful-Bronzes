import math
N = int(input())
num_list = list(map(int, input().split()))
A_ori = num_list[0]
for i in range(1, N):
  gcd_num = math.gcd(A_ori, num_list[i])
  A = A_ori//gcd_num
  B =num_list[i]//gcd_num
  if B ==0:
    B=1
  print(str(A) +"/"+str(B))