a = int(input())
num = 1 #벌집 개수
cnt = 1
while a > num:
    num += 6 * cnt
    cnt += 1
print(cnt)