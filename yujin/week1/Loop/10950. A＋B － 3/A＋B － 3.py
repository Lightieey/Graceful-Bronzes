t = int(input())
sum = []
for i in range(0,t):
  a, b = map(int, input().split())
  sum.append(a+b)
for i in range(0, t):
  print(sum[i])