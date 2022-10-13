# 수 정렬하기3
# 계수정렬

# 아마도 구글링 풀이
# 리스트 만든 후, 숫자와 동일한 인덱스에 1 삽입
# 값이 1인 인덱스를 차례로 출력
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)