import sys
N = int(sys.stdin.readline())
input_num_list = [0]*10001
for i in range(0, N):
  input_num = int(sys.stdin.readline())
  input_num_list[input_num] += 1
for i in range(1,10001):
  if input_num_list[i] != 0:
    for j in range(0, input_num_list[i]):
      print(i)