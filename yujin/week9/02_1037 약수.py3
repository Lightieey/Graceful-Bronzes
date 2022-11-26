n = int(input())
factor_list = list(map(int, input().split()))
factor_list.sort()
#factor_list
if n==1:
  print(factor_list[0]**2) # 제곱
else:
   print(factor_list[0]*factor_list[n-1]) 
