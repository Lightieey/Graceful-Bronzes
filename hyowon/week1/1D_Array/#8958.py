# OX퀴즈

import sys

N = int(sys.stdin.readline())

ox_score = []
for i in range(N):
    ox = sys.stdin.readline()
    count = 0
    seq = 0
    for j in ox:
        if j == 'O':
            seq += 1
            count += seq
        else:
            seq = 0
    ox_score.append(count)

for s in ox_score:
    print(s)


