n = int(input())
set_list = set(map(int, input().split()))
input_n = int(input())
input_list = list(map(int, input().split()))

for n in input_list:
  if(n in set_list):
    print(1, end=" ")
  else:
    print(0, end=" ")