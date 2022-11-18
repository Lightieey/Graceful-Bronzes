N = int(input())
cards = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

dic = dict()

for num in cards:
  if num in dic:
    # 기존 개수+1
    dic[num] += 1
  else:
    # 새롭게 추가
    dic[num] = 1

for target in targets:
  if target in dic:
    print(dic[target], end=' ')
  else:
    print(0, end=' ')