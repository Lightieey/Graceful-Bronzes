# A+B - 5

## EOF(-1, ctrl+z or ctrl+D) 판단 방법 2가지
## 1. 예외처리 -> except EOFError: break
## 2. readlines() 사용 -> 아래 코드

import sys

testCase_A = []
testCase_B = []
result = []

# readlines() 파일의 끝까지 가져옴
lines = sys.stdin.readlines()

# lines: 파일 전체, line: 한 줄
for line in lines:
    A, B = map(int, line.split())
    print(A+B)
