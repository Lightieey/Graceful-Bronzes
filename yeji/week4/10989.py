#계수 정렬(Counting Sort) 알고리즘
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001   #입력받는 수가 10000보다 작은 수로 제한되어 있으므로 0이 10001개 있는 리스트 생성

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1  #입력받은 수 인덱스에 +1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):  #같은 수가 반복되었을 수 있으니 for문으로 출력
            print(i)