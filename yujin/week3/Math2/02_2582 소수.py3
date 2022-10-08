# M <= num 자연수 <= N 
# num이 소수인 것 골라 소수의 합과 최솟값 찾기
def isPrimeNumber(num):
  if num==1:
    return False
  for i in range(2, num):
    # 1과 자기 자신 제외한 것들로 나눠봤을 때 나머지가 0인게 나오면 소수 아닌거임
    if num%i ==0:
      return False
  return True    

M = int(input())
N = int(input())
prime_list = []
for i in range(M, N+1):
  if isPrimeNumber(i):
    prime_list.append(i)
if not prime_list:
  print(-1)
else:
  print(sum(prime_list))
  print(prime_list[0])