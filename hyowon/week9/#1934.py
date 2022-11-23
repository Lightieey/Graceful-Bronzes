# 최소공배수
import sys

T = int(input())

def getLCM(A, B):
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

    # 최소공배수 구하기
    if A >= B:
        if A % B == 0:
            LCM = A
        else:
            LCM = A / GCD * B / GCD * GCD
    else:
        if B % A == 0:
            LCM = B
        else:
            LCM = A / GCD * B / GCD * GCD

    return int(LCM)

result = []
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    result.append(getLCM(A, B))

for res in result:
    print(res)
