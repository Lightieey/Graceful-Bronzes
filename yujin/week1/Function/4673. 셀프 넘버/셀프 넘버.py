self_num=[]
for i in range(1, 10001):
  self_num.append(i)
for i in range(1, 10001):
  for j in str(i):
    i+=int(j) # 33 +3 +3
  if i in self_num:
    self_num.remove(i)
for self_n in self_num:
  print(self_n)