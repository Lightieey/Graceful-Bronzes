N = int(input())

num_list = []
for i in range(N):
    [a, b] = map(int, input().split())   #[b,a]형태로 리스트에 저장함.
    num_list.append([b, a])

num_list.sort()  #오름차순으로 정렬

for r in range(N):
    print(num_list[r][1], num_list[r][0])  #출력할 때에는 거꾸로!
