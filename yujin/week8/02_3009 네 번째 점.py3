point3=[]
ret_x = 0
ret_y = 0

for i in range(3):
  x, y = map(int, input().split())
  point3.append([x, y])

# x축 결정
if point3[0][0] == point3[1][0]:
  # 앞의 2개 점이 x축이 같으면 나머지 점의 x축이 결정. 1, 1, 2
  ret_x = point3[2][0] # 2
elif point3[1][0] == point3[2][0]:
  # 1, 2, 2
  ret_x = point3[0][0] # 1
elif point3[0][0] == point3[2][0]:
  # 1, 2, 1
  ret_x = point3[1][0] # 2
 
 # y축 결정
if point3[0][1] == point3[1][1]:
  ret_y = point3[2][1] 
elif point3[1][1] == point3[2][1]:
  ret_y = point3[0][1] 
elif point3[0][1] == point3[2][1]:
  ret_y = point3[1][1] 

print(ret_x, ret_y)
