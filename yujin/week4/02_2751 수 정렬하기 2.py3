import sys
N = int(sys.stdin.readline())
input_num_list = []
for i in range(0, N):
  input_num_list.append(int(sys.stdin.readline()))
input_num_list.sort()
for num in input_num_list:
  print(num)