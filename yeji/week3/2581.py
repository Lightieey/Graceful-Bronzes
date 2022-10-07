min_num = int(input())
max_num = int(input())
sosu_list = []

for num in range(min_num, max_num + 1):
    error = 0
    if num > 1:
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  #소수 아님
        if error == 0:
            sosu_list.append(num)  # error가 없으면 소수리스트에 추가

if len(sosu_list) > 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)