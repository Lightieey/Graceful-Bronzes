# 알고리즘 수업 - 병합 정렬 1
import sys

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return

    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            ans.append(g1[i1])
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            ans.append(g2[i2])
            i2 += 1
            ia += 1

    while i1 < len(g1):
        a[ia] = g1[i1]
        ans.append(g1[i1])
        i1 += 1
        ia += 1

    while i2 < len(g2):
        a[ia] = g2[i2]
        ans.append(g2[i2])
        i2 += 1
        ia += 1



N, K = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

ans = []
merge_sort(N_list)

if len(ans) >= K:
    print(ans[K-1])
else:
    print(-1)


# def merge_sort(A, p, r):
#
#     if p < r:
#         q = math.floor((p + r) // 2)
#
#         merge_sort(A, p, q)  # 전반부 정렬
#         merge_sort(A, q + 1, r)  # 후반부 정렬
#         merge(A, p, q, r)  # 병합
#
# def merge(A, p, q, r):
#     i = p
#     j = q+1
#     t = 1
#     tmp = [0 for s in range(len(A))]
#     while i <= q and j <= r:
#         if A[i] <= A[j]:
#             tmp[t] = A[i]
#             t += 1
#             i += 1
#         else:
#             tmp[t] = A[j]
#             t += 1
#             i += 1
#
#     while i <= q:   # 왼쪽 배열 부분이 남은 경우
#         tmp[t] = A[i]
#         t += 1
#         i += 1
#     while j <= r:   # 오른쪽 배열 부분이 남은 경우
#         tmp[t] = A[j]
#         t += 1
#         i += 1
#     i = p
#     t = 1
#     while i <= r:   # 병합한 정렬 A에 저장
#         A[i] = tmp[t]
#         t += 1
#         i += 1