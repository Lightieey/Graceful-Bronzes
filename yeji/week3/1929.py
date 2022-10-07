M, N = map(int, input().split())

for num in range(M, N+1):
    error = 0
    if num > 1:
        for i in range(2, int(num**0.5)+1):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  #소수 아님
        if error == 0:
            print(num)  # error가 없으면 출력
