n = int(input())
numlist = list(map(int, input().split()))
if n == 1:  #약수의 개수가 1개면 그 수의 제곱이 N임.
    print(numlist[0]*numlist[0])
else:  #약수의 개수가 2개 이상이면 최소값과 최대값의 곱이 N이다.
    print(min(numlist) * max(numlist))
