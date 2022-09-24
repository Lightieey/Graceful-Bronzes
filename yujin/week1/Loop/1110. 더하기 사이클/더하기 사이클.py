import sys
num = int(sys.stdin.readline())
n=num
count=0
while True:
  a = int(n)//10
  b = int(n)%10
  sum = a+b
  new = b*10 + sum%10
  count+=1
  if num == new:
    break
  else:
    n = new
print(count)