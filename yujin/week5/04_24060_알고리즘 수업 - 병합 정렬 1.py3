from math import ceil
def merge_sort(a, order):
  n = len(a)
  if n <= 1:
    return
  mid = ceil(n / 2)
  g1 = a[:mid]
  g2 = a[mid:]
  merge_sort(g1, order) 
  merge_sort(g2, order)
  i1 = 0
  i2 = 0
  ia = 0
  while i1 < len(g1) and i2 < len(g2):
    count[0]+=1
    if g1[i1] < g2[i2]:
      a[ia] = g1[i1]
      if count[0]==order:
        print(g1[i1])
      i1 += 1
      ia += 1
    else:
      a[ia] = g2[i2]
      if count[0]==order:
        print( g2[i2])
      i2 += 1
      ia += 1
    #print(a)
  while i1 < len(g1):
    count[0]+=1
    a[ia] = g1[i1]
    if count[0]==order:
      print(g1[i1])
    i1 += 1
    ia += 1
    #print(a)
  while i2 < len(g2):
    count[0]+=1
    a[ia] = g2[i2]
    if count[0]==order:
      print( g2[i2])
    i2 += 1
    ia += 1
    #print(a)

count=[0]
arr_size, order = map(int, input().split())
arr = list(map(int, input().split()))
merge_sort(arr, order)
if count[0]<order:
  print(-1)
#print(count[0])