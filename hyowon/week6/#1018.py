# 체스판 다시 칠하기
import sys

N, M = map(int, sys.stdin.readline().split())
chess_board = []

chess_board = []
for n in range(N):
    chess_list = list(sys.stdin.readline())
    del chess_list[-1]
    chess_board.append(chess_list)

type1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
type2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

correct = []
for i in range(4):
    correct.append(type1)
    correct.append(type2)


print(chess_board)
