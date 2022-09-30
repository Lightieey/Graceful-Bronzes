num1, num2 = map(str, input().split())
num1 =  "".join(reversed(num1))
num2 =  "".join(reversed(num2))
if int(num1) > int(num2):
  print(num1)
else:
  print(num2)