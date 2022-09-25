# A, B = map(int, input().split())
# C = int(input())
# A += C // 60
# B += C % 60

# if B >= 60:
#     A += 1
#     B -= 60
# if A >= 24:
#     A -= 24
# print(A, B)

# A, B, C = map(int, input().split())

# if A == B == C:
#     print(10000 + A * 1000)

# elif A == B:
#     print(1000 + A * 100)
# elif A == C:
#     print(1000 + A * 100)
# elif B == C:
#     print(1000 + B * 100)
# else:
#     print(100 * max(A, B, C))

# A = int(input())
# for i in range(1, 10):
#     print('{} * {} ='.format(A, i), A*i)

# 10950
# A = int(input())
# for i in range(1, A+1):
#     B, C = map(int, input().split())
#     print(B + C)

# 8393
# A = int(input())
# C = 0
# for i in range(1, A+1):
#     C += i
# print(C)

# 25304
# bill = int(input())
# item = int(input())
# bill_ex = 0
# for i in range(1, item+1):
#     price, num = map(int, input().split())
#     bill_ex += price * num

# if bill == bill_ex:
#     print("Yes")
# else:
#     print("No")

# 11021
# A = int(input())
# for i in range(1, A+1):
#     B, C = map(int, input().split())
#     print('Case #{}:'.format(i), B+C)

# 11022
# A = int(input())
# for i in range(1, A+1):
#     B, C = map(int, input().split())
#     print('Case #{}: {} + {} ='.format(i, B, C), B+C)

# 2438
# A = int(input())
# for i in range(1, A+1):
#     print('*' * i)

# 2439
# A = int(input())
# for i in range(1, A+1):
#     print(' '*(A-i) + '*' * i)

# 10871
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# for i in range(N):
#     if A[i] < X:
#         print(A[i], end=" ")

# 10952
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)

# 10951
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# 1110
# N = int(input())
# num = N
# count = 0

# while True:
#     a = num//10
#     b = num % 10
#     c = (a+b) % 10
#     num = (b*10) + c
#     count += 1
#     if(num == N):
#         break
# print(count)

# cnt = int(input())
# numbers = list(map(int, input().split()))
# print(min(numbers), max(numbers))

# 2562
# numbers = [int(input()) for i in range(9)]
# print(max(numbers))
# print(numbers.index(max(numbers)) + 1)


# 3052

# numbers = []
# for i in range(10):
#     a = int(input())
#     b = a % 42
#     numbers.append(b)

# different = set(numbers)
# print(len(different))

# 1546
# n = int(input())
# score = list(map(int, input().split()))
# max_score = max(score)

# newlist = []
# for i in score:
#     newlist.append(i/max_score*100)

# newavg = sum(newlist)/n
# print(newavg)

# 8958
# n = int(input())

# for _ in range(n):
#     ox_list = list(input())
#     score = 0
#     sum_score = 0
#     for ox in ox_list:
#         if ox == 'O':
#             score += 1
#             sum_score += score
#         else:
#             score = 0  # 다시 초기화
#     print(sum_score)

n = int(input())
for i in range(n):
    score = list(map(int, input().split()))
    avg = sum(score) - score[0] / score[0]
    print(avg)

# 4344
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] * 100
    print(f'{rate:.3f}%')
