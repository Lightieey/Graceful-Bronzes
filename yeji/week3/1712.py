A, B, C = map(int, input().split())

if B >= C:   #0이나 마이너스로 나눌 수 없으니?
    print(-1)
else:
    num = A // (C - B)
    print(num+1)


# A, B, C = map(int, input().split())
# num = A // (C - B)
#
# if num <= 0:
#     print(-1)
# else:
#     print(num+1)