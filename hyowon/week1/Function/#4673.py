# 셀프 넘버

## 하다가 만 코드
double = [1,3,5,7,9,20,31,42,53,64,75,86,97]

notSelfNum = []


for n in range(0, 10001):
    if n not in notSelfNum:
        print(n)


## 구글링 코드
def d(n):
    n = n + sum(map(int, str(n)))
    return n

nonSelfNum = set()

for i in range(1, 10001):
    nonSelfNum.add(d(i))

for j in range(1, 10001):
    if j not in nonSelfNum:
        print(j)
