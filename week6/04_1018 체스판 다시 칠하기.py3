def make_board(first_W):
  if first_W:
    board = ["WBWBWBWB", 
             "BWBWBWBW",
             "WBWBWBWB", 
             "BWBWBWBW",
             "WBWBWBWB", 
             "BWBWBWBW",
             "WBWBWBWB", 
             "BWBWBWBW"]
    return board
  else:
    board = ["BWBWBWBW", 
             "WBWBWBWB", 
             "BWBWBWBW", 
             "WBWBWBWB",
             "BWBWBWBW", 
             "WBWBWBWB",
             "BWBWBWBW", 
             "WBWBWBWB",]
    return board

M, N = map(int, input().split())
board=[]
for i in range(M):
  board.append(input())

count_list=[]
count_index =-1
true_baord_W = make_board(True)
true_baord_B = make_board(False)
# 영상처리 때처럼 motion estimation
for i in range(0, M-8+1):
  for j in range(0, N-8+1):
    count_list.append(0)#W, B시작보드로 검사
    count_list.append(0)
    count_index+=1
    # 8x8씩 볼거임
    for m in range(8):
      for n in range(8):
        if true_baord_W[m][n]!=board[m+i][n+j]:
          # 일치하지 않으면 잘못칠해진 것
          count_list[count_index]+=1
        if true_baord_B[m][n]!=board[m+i][n+j]:
          count_list[count_index+1]+=1
    count_index+=1

#print(count_list)
print(min(count_list))