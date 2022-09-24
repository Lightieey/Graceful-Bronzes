import sys
n_list=[]
while True:
  try:
   n = int(sys.stdin.readline())
  except:
   break
  n_list.append(n)
nam_set=set([])
for i in n_list:
  nam_set.add(i%42)
print(len(nam_set))