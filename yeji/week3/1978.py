n = int(input())
nums = list(map(int, input().split()))
sosu = 0 #소수 개수

for i in nums:
    cnt = 0
    if(i == 1): # 1은 건너띔
        pass
    for j in range(2, i+1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        sosu += 1
print(sosu)