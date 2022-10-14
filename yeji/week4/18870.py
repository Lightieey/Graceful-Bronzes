#시간초과된 풀이
# N = int(input())
#
# num_list = list(map(int, input().split()))
#
# sort_list=list(set(num_list))      #중복제거
# sort_list.sort()  #오름차순 정렬
#
# for i in num_list:
#     print(sort_list.index(i), end=" ")  #정렬된 리스트에서의 인덱스 값 출력


N = int(input())

num_list = list(map(int, input().split()))

sort_list=list(set(num_list))      #중복제거
sort_list.sort()  #오름차순 정렬

dic = {sort_list[i] : i for i in range(len(sort_list))}
for i in num_list:
    print(dic[i], end = ' ')