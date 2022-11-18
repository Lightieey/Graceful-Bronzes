cham_num = int(input())
gil_list = []
dic={}
for i in range(6):
  bang, m = map(int, input().split())
  gil_list.append([bang, m])
  if bang in dic:
    dic[bang]+=1
  else:
    dic[bang]=1
# 딕셔너리에 각 방향 몇개인지 세어두기

totalX =0
totalY =0
subX =0
subY =0

# 어느 도형인지 딕셔너리에 세어둔 것으로 파악
if dic[1] == 2:
  # 가로로 누운 도형 중 하나
  if dic[4] ==1:
    # ㄱ 모양 도형 1
    for i in range(len(gil_list)):
      if gil_list[i][0] == 4:
        totalY=gil_list[i][1]
      elif gil_list[i][0] == 2:
        totalX=gil_list[i][1]
      elif gil_list[i][0] == 3 and gil_list[i-1][0]==1:
        subX = gil_list[i][1]
        subY = gil_list[i-1][1]
    print((totalX * totalY - subX * subY)*cham_num)

  elif dic[4]==2:
    # ㄱ 모양 y축 대칭 도형 2
    for i in range(len(gil_list)):
      if gil_list[i][0] == 3:
        totalY=gil_list[i][1]
      elif gil_list[i][0] == 2:
        totalX=gil_list[i][1]
      elif gil_list[i][0] == 1 and gil_list[i-1][0]==4:
        subX = gil_list[i][1]
        subY = gil_list[i-1][1]
    print((totalX * totalY - subX * subY)*cham_num)

elif dic[1] == 1:
  # 세로 도형 중 하나
  if dic[4] == 2:
    # L 모양 도형 3
    for i in range(len(gil_list)):
      if gil_list[i][0] == 3:
        totalY=gil_list[i][1]
      elif gil_list[i][0] == 1:
        totalX=gil_list[i][1]
      elif gil_list[i][0] == 4 and gil_list[i-1][0]==2:
        subX = gil_list[i][1]
        subY = gil_list[i-1][1]
    print((totalX * totalY - subX * subY)*cham_num)

  elif dic[4] ==1:
    # L 모양 y축 대칭 도형 4
    for i in range(len(gil_list)):
      if gil_list[i][0] == 1:
        totalY=gil_list[i][1]
      elif gil_list[i][0] == 4:
        totalX=gil_list[i][1]
      elif gil_list[i][0] == 2 and gil_list[i-1][0]==3:
        subX = gil_list[i][1]
        subY = gil_list[i-1][1]
    print((totalX * totalY - subX * subY)*cham_num)