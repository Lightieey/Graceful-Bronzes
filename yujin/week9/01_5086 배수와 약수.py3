while True:
  a, b = map(int, input().split())
  if a==0 and b==0:
    break
  
  if b % a == 0:
    # 첫 번째 숫자가 두 번째 숫자의 약수이다.
    print("factor")
  elif a % b ==0:
    # v첫 번째 숫자가 두 번째 숫자의 배수이다
    print("multiple")
  else:
    # 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
    print("neither")