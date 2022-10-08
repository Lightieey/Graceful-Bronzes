def isPrimeNumber(num):
  if num==1:
    return False
  for i in range(2, int(num**0.5)+1):
    # 1과 자기 자신 제외한 것들로 나눠봤을 때 나머지가 0인게 나오면 소수 아닌거임
    if num%i ==0:
      return False
  return True 

test_case = int(input())
for i in range(0, test_case):
  num = int(input())
  a, b = num//2, num//2
  while a > 0:
    if isPrimeNumber(a) and isPrimeNumber(b):
      print(a, b)
      break
    else:
      a -= 1
      b += 1   