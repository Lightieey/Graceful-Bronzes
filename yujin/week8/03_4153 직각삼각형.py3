
while True:
  isZigGac = False
  x, y, z = map(int, input().split())
  if x==0 and y==0 and z==0:
    break
  
  if x**2 == y**2 + z**2:
    isZigGac=True
  elif y**2 == x**2 + z**2:
    isZigGac=True
  elif z**2 == x**2 + y**2:
    isZigGac=True
  
  if isZigGac:
    print("right")
  else:
    print("wrong")
