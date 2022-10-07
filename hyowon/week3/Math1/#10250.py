# ACM 호텔
import sys

T = int(sys.stdin.readline())

case_List = []
for i in range(T):
    case = list(map(int, sys.stdin.readline().split()))
    case_List.append(case)

for c in case_List:
    if c[2] % c[0] == 0:
        floor = c[0]
        number = c[2] // c[0]
    else:
        floor = c[2] % c[0]
        number = c[2] // c[0] + 1
    if number < 10:
        house = str(floor) + "0" + str(number)
    else:
        house = str(floor) + str(number)
    print(house)
