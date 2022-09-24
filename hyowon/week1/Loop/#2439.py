# 별 찍기 - 2
import sys

N = int(sys.stdin.readline())

## 출력 형식이 잘못되었습니다. 오류 뜸
# for i in range(0, N):
#     for j in range(0, N-i):
#         print(' ', end='')
#     for j in range(0, i+1):
#         print('*', end='')
#     print('')

## 다른 풀이(구글링)
for i in range(0, N):
    print(" "*(N-i)+"*"*i)

## 범위 지정 주의 !!!
## range(0, N)으로 지정시 -> " "*N 출력, "*"*N 출력 안함
