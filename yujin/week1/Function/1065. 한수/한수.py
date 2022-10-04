import sys
n = int(sys.stdin.readline())
count=0
for i in range(1, n+1):
  if i <10:
    count+=1
  elif i >=10 and i <100:
    count+=1
  elif i >=100 and i <1000:
    num = str(i)
    if (int(num[0])-int(num[1]))==(int(num[1])-int(num[2])):
      count+=1  
print(count)