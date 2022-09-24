h, m = map(int, input().split())
time = h*60 + m - 45
# 만약 time이 음수값이 된다면
if time<0:
  h=23
  m=60+time
else:
  h = time//60
  m = time%60
print(h, m)
