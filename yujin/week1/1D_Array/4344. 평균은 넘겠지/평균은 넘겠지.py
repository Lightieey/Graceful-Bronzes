import sys
C = int(input())
N=0

for i in range(0, C):
  score_list = list(map(int, input().split()))
  N = score_list.pop(0) # 학생수
  count = 0
  sum =0
  for score in score_list:
    sum+= score
  m = sum/N
  for score in score_list:
    if score>m:
      count+=1
  print("{:,.3f}%".format(round((count/N)*100, 3)))
