N = int(input())
# 자연수 N이니까 1부터 N까지 돌면서 확인해주면 됨
for num in range(1, N+1):
  # 하나씩 더해보면 됨^^
  # 일단 각 자리들 구하는 것
  n_list = list(map(int, str(num)))
  if sum(n_list, num) == N:
    print(num)
    exit(0)
    break
print(0)