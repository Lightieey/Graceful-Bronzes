# N은 홀수 
#import numpy as np
from collections import Counter
import sys
#N = int(input())
N = int(sys.stdin.readline())
input_num_list=[]
for i in range(0, N):
  #input_num_list.append(int(input()))
  input_num_list.append(int(sys.stdin.readline()))
# 산술평균
print(round(sum(input_num_list)/len(input_num_list)))

# 중앙값
#print(int(np.median(input_num_list)))
sorted_input_list = sorted(input_num_list) # 증가 순서 나열, 오름차순
print(sorted_input_list[len(sorted_input_list)//2]) # 중앙 위치 값
#  Counter 클래스의 most_common() 메쏘드는 등장한 횟수를 내림차순으로 정리
# 리스트(list)를 구성하는 요소들은 튜플(tuple)인데, 
# 각 튜플의 첫 번째 요소는 numbers에 등장하는 숫자이고, 두 번째 요소는 각 숫자가 등장한 횟수
count = Counter(input_num_list)
mode = count.most_common() # 여기 값을 주면 상위 n개까지 뽑아줌
# print(mode) # 최빈값부터 쭉 내림차순으로
# 최빈값들만 뽑아주는 과정
max_count = mode[0][1]
modes = []
for num in mode:
  if num[1] == max_count:
    modes.append(num[0])
# 여기까지 오면 최빈값들만 모인거 (수, 횟수)에서 num[0]는 수
if len(modes)>1:
  modes.sort() # 튜플 첫번째 요소로 오름차순 정렬
  #print(modes)
  # 최빈값 중 두번째로 작은 것 출력 
  print(modes[1])
else:
  print(modes[0])
print(abs(max(input_num_list)-min(input_num_list)))