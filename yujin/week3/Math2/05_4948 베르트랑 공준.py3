# 테스트 케이스 총 범위
n=123456

def isPrimeNumber(num):
  if num==1:
    return False
  for i in range(2, int(num**0.5)+1):
    # 1과 자기 자신 제외한 것들로 나눠봤을 때 나머지가 0인게 나오면 소수 아닌거임
    if num%i ==0:
      return False
  return True    

# 에라토스테네스의 체
primes_list = list(range(2,246912))
ans_list = []

for i in primes_list:
  # 만약 소수에 해당하면 prime_list 함수에서 true를 반환 받어
  if isPrimeNumber(i):
    # true를 반환 받는다면 ans_list에 해당 원소(i)를 추가
    ans_list.append(i) # 소수만 있어
        
        
while True:
    
  count = 0

  num = int(input())

  # 0을 입력받으면 종료    
  if num == 0:
    break
  
  for i in ans_list:
    if num < i < 2*num+1:
      count += 1
            
  print(count)