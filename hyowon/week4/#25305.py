# 커트라인
import sys

N, k = map(int, sys.stdin.readline().split())

scoreList = list(map(int, sys.stdin.readline().split()))

scoreList.sort(reverse=True)

print(scoreList[k-1])