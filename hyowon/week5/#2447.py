# 별 찍기 - 10

# 구글링 코드
import sys

def draw_stars(n):
    if n == 1:
        return ['*']

    Stars = draw_stars(n//3)
    L = []

    for star in Stars:
        L.append(star*3)
    for star in Stars:
        L.append(star+' '*(n//3)+star)
    for star in Stars:
        L.append(star*3)

    return L

N = int(sys.stdin.readline())
print('\n'.join(draw_stars(N)))

# def star_recur(x, y):
#     if x == 1 and y == 1:
#         print(' ', end=' ')
#     elif 0 <= x < 3 and 0 <= y < 3:
#         print('*', end=' ')
#
#     # elif x == 3 and y == 3:
#     #     for i in range(3):
#     #         for j in range(3):
#     #             # a = i // (x/3)
#     #             # b = j // (y/3)
#     #             star_recur(i%3, j%3)
#     #         print('')
#
#     elif x >= 3 and y >= 3:
#         for i in range(3):
#             for j in range(3):
#                 if i == 1 and j == 1:
#                     star_recur(x // 3, y // 3)
#                 else:
#                     star_recur(i+x, y // 3)
#             print('')
#         x //= 3
#         y //= 3
#     # elif x >=3 and y >= 3:
#     #     for i in range(3):
#     #         for j in range(3):
#     #             star_recur(i // x//3, y//3)
#
# star_recur(9, 9)