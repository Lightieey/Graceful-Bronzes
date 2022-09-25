# 알파벳 찾기

import sys

S = sys.stdin.readline()

alphabet = "abcdefghijklmnopqrstuvwxyz"

countNum = []

for s in alphabet:
    countNum.append(S.find(s))

for c in countNum:
    print(c, end=' ')

# 문자열 위치 찾는 함수 index(), find()
# 해당 문자열이 존재하지 않을 때 index()는 오류를 출력, find()는 -1을 출력