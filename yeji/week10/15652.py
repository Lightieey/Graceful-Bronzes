#백트래킹 - 깊이 우선 탐색
# s : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
#             출력    pop(2)    출력   pop(3)    출력

n, m = map(int, input().split())

s = []


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()


dfs(1)