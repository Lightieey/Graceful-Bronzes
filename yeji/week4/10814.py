N = int(input())
member_list = []
for i in range(N):
    [age, name] = map(str, input().split())  #[나이, 이름] 형태로 리스트에 저장
    member_list.append([age, name])

member_list.sort(key=lambda x: int(x[0]))   #나이 순으로 정렬
for r in range(N):
    print(member_list[r][0], member_list[r][1])

# N = int(input())
# member_list = []
# for i in range(N):
#     age, name = map(str, input().split())
#     age = int(age)
#     member_list.append((age, name))
#
# member_list.sort(key = lambda x : x[0])
#
# for r in member_list:
#     print(r[0], r[1])