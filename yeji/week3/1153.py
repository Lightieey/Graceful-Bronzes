N = int(input())
m = 2
while N!=1:  #나머지가 1일때까지
  if N%m==0: 
    print(m) 
    N = N//m
  else:
    m += 1  #소수가 아닐 수 없음