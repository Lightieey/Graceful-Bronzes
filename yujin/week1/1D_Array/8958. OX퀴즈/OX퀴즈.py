import sys
n = int(sys.stdin.readline())
for i in range(0, n):
  sum =0
  count = 0
  score_list = sys.stdin.readline()
  for ox in score_list:
    if ox == "O":
      count+=1
      sum+=count
    else:
      count = 0
  print(sum)
