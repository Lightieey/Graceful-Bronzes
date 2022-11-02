# 분해합
# 99 -> 99 + 9 + 9 -> 117
# 117
import sys

# N의 생성자
number = []

# N
N = int(sys.stdin.readline())

cons = 0
for i in range(N):
    n = list(str(i))

    n_sum = 0
    for num in n:
        n_sum += int(num)

    if i + n_sum == N:
        cons = i
        break

print(cons)
    # number.clear()
    # num_sum = 0
    #
    # for j in range(len(n)-1, -1, -1):
    #     number.append(n[j])
    #
    # k = 0
    # for num in number:
    #     num_sum += int(num)
    #     k += 1




# if N < 10:
#     print(0)
# elif N < 100:
#     for i in range(11, N+1):
#         a = i // 10
#         b = i % 10
#         if i + a + b == N:
#             print(i)
#             break
#         if i == N and i + a + b != N:
#             print(0)





