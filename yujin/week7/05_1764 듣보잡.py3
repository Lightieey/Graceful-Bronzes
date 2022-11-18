N, M = map(int, input().split())
dic = dict()
d_list = [] #듣지못한 애들
db_list=[]
for i in range(N):
  d_list.append(input())

# 시간초과 싫어어어어
for d in d_list:
  dic[d]=1

for j in range(M):
  name = input()
  if name in dic:
    db_list.append(name)

db_list.sort()
print(len(db_list))
for db in db_list:
  print(db)