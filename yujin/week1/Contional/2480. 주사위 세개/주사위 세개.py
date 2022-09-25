a, b, c = map(int, input().split())
won = 0
if a==b and b==c and c==a:
  won = 10000+a*1000
elif a==b:
  won = 1000+a*100
elif a==c:
  won = 1000+a*100
elif b==c:
  won = 1000+b*100
else:
  won = max(a, b, c)*100
print(won)