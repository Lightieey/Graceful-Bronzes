def apt(k, n, count, apt_k_list):
  if k<=count:
    # k층보다 위이면 끝냄. 리스트의 가장 마지막 원소가 k층 n호의 주민수. n-1하면 마지막 원소
    return apt_k_list[n-1]
  else:
    for i in range(0, len(apt_k_list)):
      # 이전 층수 리스트에서 가져와서 그 층수 리스트를 현재 층수로 업데이트 시켜주는 과정
      if i ==0:
        # 1호인 경우 전부 다 1이어서 그냥 엄어감
        pass
      else:
        # 2호부터는 직전 앞의 호수 더해진 것과 자기 바로 아래층만 더해주고 리스트 업데이트
        apt_k_list[i] = apt_k_list[i-1] + apt_k_list[i]
  count+=1
  return apt(k, n, count, apt_k_list)

test_case = int(input())
for i in range(0, test_case):
  k = int(input()) # k층
  n = int(input()) # n호
  count = 0 # 0층부터 올라갈 용도
  apt_k_list = [i for i in range(1, n+1)] # 초기 0층의 1~n호
  print(apt(k, n, count, apt_k_list))