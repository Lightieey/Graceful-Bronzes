# 참외밭
import sys

K = int(input())

dir_list = []
len_list = []
for i in range(6):
    dir, len = map(int, sys.stdin.readline().split())
    dir_list.append(dir)
    len_list.append(len)

# 육각형 종류 알아내기 위한 방향 리스트
dir_kind = []
for i in range(4):
    c = dir_list.count(i+1)
    if c > 1:
        dir_kind.append(i+1)

dir_str = ''.join(map(str, dir_list))

if dir_kind == [1, 3]:
    w_idx = dir_list.index(2)
    h_idx = dir_list.index(4)
    t = len_list[h_idx] * len_list[w_idx]
    #3131
    if '13' in dir_str:
        idx = dir_list.index(1)
        s = len_list[idx] * len_list[idx + 1]
    else:
        s = len_list[0] * len_list[-1]
    print((t - s)*K)

elif dir_kind == [2, 3]:
    w_idx = dir_list.index(1)
    h_idx = dir_list.index(4)
    t = len_list[h_idx] * len_list[w_idx]
    #2323
    if '32' in dir_str:
        idx = dir_list.index(3)
        s = len_list[idx] * len_list[idx + 1]
    else:
        s = len_list[0] * len_list[-1]
    print((t - s)*K)

elif dir_kind == [1, 4]:
    w_idx = dir_list.index(2)
    h_idx = dir_list.index(3)
    t = len_list[h_idx] * len_list[w_idx]
    # 1414
    if '41' in dir_str:
        idx = dir_list.index(4)
        s = len_list[idx] * len_list[idx + 1]
    else:
        s = len_list[0] * len_list[-1]
    print((t - s)*K)

elif dir_kind == [2, 4]:
    w_idx = dir_list.index(1)
    h_idx = dir_list.index(3)
    t = len_list[h_idx] * len_list[w_idx]
    # 4242
    if '24' in dir_str:
        idx = dir_list.index(2)
        s = len_list[idx] * len_list[idx + 1]
    else:
        s = len_list[0] * len_list[-1]
    print((t - s)*K)
