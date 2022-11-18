import math

T = int(input())
for t in range(T):
  count=0
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  for i in range(n):
    cx, cy, r =  map(int, input().split())
    # cx, cy 원에서 x1, y1과 x2, y2 포함되는지 확인하는 부분
    if (math.pow(r, 2) >= (math.pow(x1 - cx, 2) + math.pow(y1 - cy, 2))) and (math.pow(r, 2) >= (math.pow(x2 - cx, 2) + math.pow(y2 - cy, 2))):
      pass
    elif (math.pow(r, 2) >= (math.pow(x1 - cx, 2) + math.pow(y1 - cy, 2))):
      count+=1
    elif (math.pow(r, 2) >= (math.pow(x2 - cx, 2) + math.pow(y2 - cy, 2))):
      count+=1
  print(count)