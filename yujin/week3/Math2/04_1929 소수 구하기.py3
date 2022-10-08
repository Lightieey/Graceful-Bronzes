# M <= num 자연수 <= N
# 제곱근까지만 검사해주면 되는거였음!!!!!!!!!!!!! 
from math import sqrt
def isPrimeNumber(num):
  if num==1:
    return False
  for i in range(2, int(sqrt(num))+1):
    # 1과 자기 자신 제외한 것들로 나눠봤을 때 나머지가 0인게 나오면 소수 아닌거임
    if num%i ==0:
      return False
  return True    

M, N = map(int, input().split())
prime_list = []
for i in range(M, N+1):
  if isPrimeNumber(i):
    print(i)