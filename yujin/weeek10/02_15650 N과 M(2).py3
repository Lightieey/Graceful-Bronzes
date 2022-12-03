import itertools
n,m = list(map(int,input().split()))
num =[]
for i in range(1, n+1):
  num.append(i)
p = itertools.combinations(num, m) # 조합
p_list = list(p)
p_list.sort(key=lambda x:x[0])
#print(p_list)
for i in p_list:
  for j in range(m):
    print(i[j], end=" ")
  print()