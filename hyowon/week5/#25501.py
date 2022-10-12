# 재귀의 귀재

# 전역변수 사용법
# 함수 밖에서도 안에서도 global이라고 선언해주어야 한다.
import sys

global cnt
cnt = 0
def recursion(s, l, r):
    global cnt
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        cnt += 1
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    global cnt
    cnt += 1
    return recursion(s, 0, len(s)-1)


T = int(sys.stdin.readline())
S = []
for s in range(T):
    S.append(input())


for s in S:
    print(isPalindrome(s), end=' ')
    print(cnt)
    cnt = 0