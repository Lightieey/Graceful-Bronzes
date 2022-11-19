#시간초과
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# qnt = 0
# dict = []
# result = []
# for i in range(1, n+1):
#     a = input().rstrip()
#     dict.append(a)
#
# for i in range(m):
#     quest = input().rstrip()
#     if quest in dict:
#         qnt +=1
#         result.append(quest)
#     else:
#         pass
#
# print(qnt)
# for r in result:
#     print(r, end="\n")


N , M = map(int,input().split())
arr_1 = set()
arr_2 = set()

for _ in range(N):
    arr_1.add(input())
for _ in range(M):
    arr_2.add(input())

arr = sorted(list(arr_1 & arr_2))
print(len(arr))

for i in arr:
    print(i)
