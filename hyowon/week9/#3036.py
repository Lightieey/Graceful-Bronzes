# 링
import sys

# 최대공약수 구하는 함수
def getGCD(A, B):

    ap = set()
    bp = set()

    # A의 약수 구하기
    i = 1
    while i <= A:
        if A % i == 0:
            ap.add(i)
        i += 1
    # B의 약수 구하기
    j = 1
    while j <= B:
        if B % j == 0:
            bp.add(j)
        j += 1

    # 최대공약수 구하기(겹치는 약수 중 가장 큰 것)
    ab_bp_inter = ap.intersection(bp)
    GCD = max(ab_bp_inter)

    return GCD

N = sys.stdin.readline()

Ring_List = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(Ring_List)):
    if Ring_List[0] % Ring_List[i] == 0:
        print(Ring_List[0] // Ring_List[i], end='')
        print('/', end='')
        print(1)
    else:
        GCD = getGCD(Ring_List[0], Ring_List[i])
        print(int(Ring_List[0] / GCD), end='')
        print('/', end='')
        print(int(Ring_List[i] / GCD))
