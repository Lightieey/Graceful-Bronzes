# 나는야 포켓몬 마스터 이다솜

# isdigit() : 문자열 숫자 판별

import sys

N, M = map(int, sys.stdin.readline().split())

pokemon_list = []
for i in range(N):
    pokemon_list.append(input())


input_list = []
for i in range(M):
    input_list.append(input())

for i in input_list:
    if i.isdigit():
        print(pokemon_list[int(i)-1])
    else:
        print(pokemon_list.index(i)+1)
