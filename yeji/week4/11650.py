N = int(input())

num_list = []
for i in range(N):
    [a, b] = map(int, input().split())   #[a,b]형태로 리스트에 저장함. ex. [[a,b],[a2,b2]]
    num_list.append([a, b])

num_list.sort()  #오름차순으로 정렬

for r in range(N):
    print(num_list[r][0], num_list[r][1]) 
