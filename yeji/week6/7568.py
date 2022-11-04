n = int(input())
number_list = []
for i in range(n):
    [x, y] = map(int, input().split())
    number_list.append([x, y])

for i in number_list:
    rank = 1
    for j in number_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")
