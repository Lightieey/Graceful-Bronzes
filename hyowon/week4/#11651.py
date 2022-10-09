# 좌표 정렬하기2
import sys

N = int(sys.stdin.readline())

list_xy = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())

    list_xy.append([x, y])

# 람다 사용법 구글링
# y좌표(리스트[1]) 기준으로 정렬
# y좌표가 같으면 x좌표(리스트[0]) 기준으로 정렬
list_xy.sort(key=lambda x: (x[1], x[0]))

for xy in list_xy:
    print(' '.join(str(s) for s in xy))

