# 과제 안 내신 분..?
import sys

s_list = []
for i in range(28):
    s_list.append(int(sys.stdin.readline()))

s_list.sort()

for i in range(28):
    if i == 0:
        if s_list[0] != 1:
            print(1)

    if i < 27:
        if s_list[i]+1 != s_list[i+1]:
            print(s_list[i]+1)

    if i == 27:
        if s_list[27] != 30:
            print(30)
