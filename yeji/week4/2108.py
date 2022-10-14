N = int(input())
num_list = []
for i in range(N):
    a = int(input())
    num_list.append(a)  # 숫자 받아서 리스트로 저장

#평균(소수점 첫째 자리 수까지 반올림)
num1 = round(sum(num_list)/N, 1)
print(num1)

#중앙값
num2 = num_list[N//2]
print(num2)

#최빈값

#범위
num4 = max(num_list) - min(num_list)