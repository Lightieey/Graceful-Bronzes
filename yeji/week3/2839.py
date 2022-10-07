# N = int(input())
# a = 0 #3키로 봉지 개수
# b = 0 #5키로 봉지 개수
#
# if N % 5 == 0:
#     b = N //5
#     N = N % 5
#     if N % 3 == 0:
#         a = N // 5
#         print(a + b)
# elif N % 3 == 0:
#     a = N // 3
#     print(a)
# else:
#     print(-1)
#

n = int(input()) # 설탕

result = 0 # 봉지 수

while n >= 0:
    if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
        result += n // 5 # 5로 나눈 몫 추력
        print(result)
        break
    n -= 3 # 설탕이 5의 배수가 될때까지 반복
    result += 1 # 봉지 추가
else:
    print(-1) # while문이 거짓이 되면 -1 출력