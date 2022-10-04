# 달팽이는 올라가고 싶다
import math
import sys

A, B, V = map(int, sys.stdin.readline().split())

# 하루에 달팽이가 올라갈 수 있는 높이 : A-B
# 만약 하루에 1m씩 올라갈 때
# 0->2->1, 1->3->2, 2->4->3, 3->5 (정상)
# 중간값, 즉 낮에 이미 정상에 도달했을 때, 밤은 고려되지 않음
# 낮을 기준으로 정상 도달여부를 계산

d = math.ceil((V-A)/(A-B)+1)

print(d)



