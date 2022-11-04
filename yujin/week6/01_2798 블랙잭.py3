N, M = map(int, input().split())
num_list = list(map(int, input().split()))
max_sum = 0
for i in range(0, N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      # 진짜 하나씩 다 확인할거임
      sum = num_list[i] + num_list[j] + num_list[k]
      if sum > M:
        # 크면 계속 진행
        continue
      else:
        max_sum = max(max_sum, sum)
        # 합한거랑 기존 가장 큰 값 유지하는 것 비교하여 큰값 유지
print(max_sum)