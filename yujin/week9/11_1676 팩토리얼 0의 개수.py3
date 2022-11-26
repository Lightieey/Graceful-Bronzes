import math
N = int(input())
fact = str(math.factorial(N))
count=0
#print(fact)
for i in range(len(fact)-1, -1, -1):
  if fact[i]=="0":
    count+=1
    #print(count)
  else:
    print(count)
    break