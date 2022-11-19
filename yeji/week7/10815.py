#시간초과
# N = int(input())
# cardlist = list(map(int, input().split()))
# M = int(input())
# numlist = list(map(int, input().split()))
# result = []
# for i in numlist:
#     if i in cardlist:
#         result.append(1)
#     else:
#         result.append(0)
#
# for j in range(len(result)):
#     print(result[j], end=' ')


#이진탐색
import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))
card.sort()

def binary_search(array, target, start, end):
    while start <= end:   #탐색할 범위가 남아 있는 동안 반복
        mid = (start + end) // 2 #탐색 범위의 중간 위치

        if array[mid] == target:
            return mid              #찾으면 위치 반환
        elif array[mid] > target:
            end = mid - 1           #찾는 값이 더 작으면 왼쪽으로 범위를 좁혀 계속 탐색
        else:
            start = mid + 1         #찾는 값이 더 크면 오른쪽으로 범위를 좁혀 계속 탐색
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:   #위치가 있으면
        print(1, end=' ')
    else:
        print(0, end=' ')


