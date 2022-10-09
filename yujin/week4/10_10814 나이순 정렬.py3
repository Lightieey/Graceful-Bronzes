import sys
#N = int(input())
N = int(sys.stdin.readline())
member_list=[]
for order in range(0, N):
  #age, name = map(str, input().split())
  age, name = map(str, sys.stdin.readline().split())
  member_list.append((order, age, name)) # 가입순서, 나이, 이름으로 튜플로 저장
member_list.sort(key=lambda x : (int(x[1]), x[0])) # x[1]은 age 나이 순, 나이 같으면 x[0]인 order 가입한 순서
for member in member_list:
  print(member[1], member[2])