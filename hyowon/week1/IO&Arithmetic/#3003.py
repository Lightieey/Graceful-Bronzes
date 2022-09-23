# 킹, 퀸, 룩, 비숍, 나이트, 폰

import sys

chess_list = [1,1,2,2,2,8]

# input()보다 stdin.readline()을 이용하는 것이 훨씬 빠르다.
dongHyuk_list = list(map(int, sys.stdin.readline().split()))


for i in range(0, len(dongHyuk_list)):
    print(chess_list[i]-dongHyuk_list[i], end=' ')