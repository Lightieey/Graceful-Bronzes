N, M = map(int, input().split())
string_set =set()
#string_input_list = []
count = 0
for i in range(N):
  string_set.add(input())
for j in range(M):
  #string_input_list.append(input())
  if(input() in string_set):
    count+=1
print(count)

