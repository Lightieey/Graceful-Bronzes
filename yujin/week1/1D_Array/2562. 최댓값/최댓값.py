import sys
n_list=[]
while True:
  try:
   n = int(sys.stdin.readline())
  except:
   break
  n_list.append(n)
print(max(n_list))
print(n_list.index(max(n_list))+1)