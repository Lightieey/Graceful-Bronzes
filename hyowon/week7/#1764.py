# 듣보잡

# 집합 메소드
# add : 원소 추가
# update : 원소 여러개 추가
# remove, discard : 원소 삭제
# union, intersection, difference

# sorted와 sort의 차이
# sorted : 새로 정렬된 출력
# sort : 원래 목록 자체 요소 정렬

import sys

N, M = map(int, sys.stdin.readline().split())

# 공집합 선언시 heard = {}하면, 공집합이 아닌 딕셔너리를 생성
heard = set()
for i in range(N):
    heard.add(input())

saw = set()
for j in range(M):
    saw.add(input())

saw_heard = list(heard.intersection(saw))

saw_heard.sort()

print(len(saw_heard))
for sh in saw_heard:
    print(sh)

