# 부녀회장이 될테야

# 규칙
# 1. 각 호의 사람 수가 0층의 2호 꼭짓점을 기준으로 대각선 대칭이다.
#    - 0층의 2호~14호와 모든 2호의 사람 수는 2,3,4,5 ..로 증가한다.
# 2. 각 호의 사람 수는 옆집과 아랫집을 더한 합이다.
# 3. 모든 1호의 사람 수는 1이다.

# 1 ...
# 1 5 ...
# 1 4 10 ...
# 1 3 6  10 ...
# 1 2 3  4  5 ...


import sys

def countPeople(kp, np):
    if kp == 0:
        return np
    elif np == 2:
        return kp+2
    elif np == 1:
        return 1
    else:
        return countPeople(kp, np-1) + countPeople(kp-1, np)

T = int(sys.stdin.readline())

k_List = []
n_List = []
for t in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    k_List.append(k)
    n_List.append(n)

for i in range(T):
    print(countPeople(k_List[i], n_List[i]))

