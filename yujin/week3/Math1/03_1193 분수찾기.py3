# 대각선으로 잘만 보면 벌집이랑 비슷한 문제임!
n = int(input())
honeycomb = 0
step = 0
while n > honeycomb:
  # n이 벌집 현재 개수보다 크면 한단계 더 나아가서 벌집을 키움
  honeycomb+=step # 이번에는 대각선 지날 때마다 1개 2개 3개 4개 순차적으로 증가함
  step+=1
  # 몇번 증가되다 보면 honeycomb 벌집 크기보다 n이 작아지는 시점 옴. 그때는 while문 돌지 않고 나와
# 여기까지 나온 step이 대각선에서 분수의 분모, 분자 합
# honeycomb가 X가 해당되는 대각선에서 가장 마지막 숫자와 동일해짐
# 11 입력시 step 6, honeycomb 15 나옴
#print(step)
#print(honeycomb)
#step-1개의 숫자가 대각선에 존재, 11입력시 5개 존재
sub = honeycomb - n # 대각선의 가장 끝 수로부터 얼마나 떨어져 있는지
# 13 입력시 sub = 15 -13 해서 2가 나옴
if step%2 == 0:
  # 합이 짝수일 때는 순회가 다름
  print( "%d/%d" %(1 + sub,(step-1)-sub))
elif step%2 != 0:
  print( "%d/%d" %((step-1)-sub,1 + sub))