# 평균은 넘겠지
import sys

# 테스트 케이스 수
C = int(sys.stdin.readline())

# 학생수 N과 N명의 학생 점수들 포함 리스트 -> case
N = 0
p_list = []

for i in range(C):
    case = list(map(int, sys.stdin.readline().split()))
    N = case[0]
    sum = 0
    for j in range(1, N+1):
        sum += case[j]
    avg = sum / N

    st_num = 0
    for k in range(1, N+1):
        if case[k] > avg:
            st_num += 1

    processpoint = st_num/N*100
    p_list.append(processpoint)

for p in p_list:
    print("%0.3f%%" % p)

## 파이썬 퍼센티지 표시 방법 %%





