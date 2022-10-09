import sys
#N = int(input())
N = int(sys.stdin.readline())
num_list = []
for i in range(0, N):
  #x, y = map(int, input().split())
  x, y = map(int, sys.stdin.readline().split())
  num_list.append((x, y))
num_list.sort(key= lambda x : (x[1], x[0]) ) 
# x[1]인 y 요소로 오름차순 정렬 후, 그 결과로 x[0]요소로 오름차순 정렬
for num in num_list:
  print(num[0], num[1])