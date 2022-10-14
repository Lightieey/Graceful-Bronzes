n = int(input())
num_list = []
for i in str(n):  #str반복하면서 리스트에 넣음
    num_list.append(int(i))

num_list.sort(reverse=True)  # 내림차순

for i in num_list:
    print(i, end='')