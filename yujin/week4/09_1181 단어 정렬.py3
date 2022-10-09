import sys
N = int(input())
#N = int(sys.stdin.readline())
voca_list = []
for i in range(0, N):
  voca_list.append(input())
  #voca_list.append(sys.stdin.readline())
voca_set = set(voca_list) # 중복 제거
#print(voca_set)
del voca_list
voca_list = list(voca_set)
voca_list.sort(key= lambda x : (len(x), x)) # 길이로 정렬하고, 같으면 사전순
for voca in voca_list:
  print(voca)