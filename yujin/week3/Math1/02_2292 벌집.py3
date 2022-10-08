n = int(input())
honeycomb = 1
step = 1
while n > honeycomb:
  # n이 벌집 현재 개수보다 크면 한단계 더 나아가서 벌집을 키움
  honeycomb+=6*step # 키울 때 벌집은 step (방 나아가는 개수)에 따라 6의 배수씩 증가
  step+=1
  # 몇번 증가되다 보면 honeycomb 벌집 크기보다 n이 작아지는 시점 옴. 그때는 while문 돌지 않고 나와
print(step)