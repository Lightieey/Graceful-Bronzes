N = int(input())
dungchi = []
for i in range(N):
  x, y = map(int, input().split())
  dungchi.append([x, y, 1])
  # x, y, 덩치
for i in range(0, len(dungchi)):
  # 인덱스i번째인 애를 기준으로 검사
  for j in range(0, len(dungchi)):
    if (dungchi[i][0]  < dungchi[j][0])and (dungchi[i][1] < dungchi[j][1]):
      # x, y 둘다 작으면 덩치 up
      dungchi[i][2] += 1
for d in dungchi:
  print(d[2], end=" ")
    