def isPrimeNumber(num):
  if num==1:
    return False
  for i in range(2, num):
    # 1과 자기 자신 제외한 것들로 나눠봤을 때 나머지가 0인게 나오면 소수 아닌거임
    if num%i ==0:
      return False
  return True    


N = int(input())
count = 0
num_list = list(map(int, input().split()))
for i in range(0, N):
  if isPrimeNumber(num_list[i]):
    count+=1
print(count)    
