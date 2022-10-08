# 3kg 5kg Nkg배달, 최대한 적은 봉지 들고가기. 정확히 Nkg
# 5A+ 3B = N (A>=B) 구해야 하는 것 몇 봉지 = A+B
N = int(input())
# 그니까 뭔가 아니다 싶으면 뒤로 빽해야한다는거 아니야?
isN = False
sum = 0
for i in range(0, (N//5)+1):
  for j in range(0, (N//3)+1):
    if 5*i+3*j==N:
      isN = True
      sum = i+j
      break
if isN:
  print(sum)
else:
  print(-1)      