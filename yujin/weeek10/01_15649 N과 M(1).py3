import itertools
n,m = list(map(int,input().split()))
num =[]
for i in range(1, n+1):
  num.append(i)
p = itertools.permutations(num, m) # 순열
#print(list(p))
for i in list(p):
  for j in range(m):
    print(i[j], end=" ")
  print()