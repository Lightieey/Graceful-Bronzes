import sys
#N = int(input())
#num_list = list(map(int, input().split()))
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

num_set = set(num_list) # 중복 제거
sort_num_list = list(num_set) # sort 쓰려고 list로 변환
sort_num_list.sort() # 현재 인덱스 위치한 나보다 작은 것들 개수 세어야 해서 오름차순
# 4, 2, 1 이게 1, 2, 4 이렇게 sort되는데 2면 자기 인덱스가 1이고, 자기 앞에 1개 작은게 있는 것이 됨.
# 그러면 num_list에서 2로 sort_num_list의 인덱스를 찾아오면 됨.
num_dict = {}
for i in range(len(sort_num_list)):
  num_dict[sort_num_list[i]]=i # 숫자 : 작은거 개수
for num in num_list:
  # 여기를 index로 찾아오는게 아니라 음
  # num이면 => 이거다 음 아 
  print(num_dict[num], end = " ")