from math import sqrt
while True:
    num = int(input())
    if num == 0:
        break
    sosu = 0  # 소수 개수
    for i in range(num+1, num*2+1):
        cnt = 0
        if (i == 1):  # 1은 건너띔
            pass
        for j in range(2, int(sqrt(i))+1):
            if (i % j == 0):
                break
        else:
            sosu += 1
    print(sosu)

