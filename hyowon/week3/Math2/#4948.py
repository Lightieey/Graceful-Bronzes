# 베르트랑 공준
import sys

case_List = []
while True:
    case = int(sys.stdin.readline())
    if case == 0:
        break
    case_List.append(case)

count_List = []
for case in case_List:
    count = 0
    for c in range(case+1, 2*case+1):
        flag = 1
        if c == 1:
            flag = 0
        else:
            for i in range(2, c):
                if c % i == 0:
                    flag = 0
                    break
        if flag == 1:
            count += 1
    count_List.append(count)

for count in count_List:
    print(count)

