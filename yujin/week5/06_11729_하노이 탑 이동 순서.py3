def Hanoi(N, from_pos, to_pos, via_pos, move_list):
  move_list[0]+=1
  if N == 1: # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
    #print( from_pos, "번 기둥에 있는 원반을 ", to_pos, "번 기둥으로 옮긴다." )
    move_list.append([from_pos, to_pos])
    return 
  Hanoi(N - 1, from_pos, via_pos, to_pos, move_list)
  #print( from_pos, " 번 기둥에 있는 원반을 ", to_pos, "번 기둥으로 옮긴다." )
  move_list.append([from_pos, to_pos])
  Hanoi(N - 1, via_pos, to_pos, from_pos, move_list)
  
move_list=[0] # 제일 첫번째 요소가 count
Hanoi(int(input()), 1, 3, 2, move_list)
for i in range(len(move_list)):
  if i==0:
    print(move_list[0])
  else:
    print(move_list[i][0], move_list[i][1])