# 층수 N%H: N번째 손님을 H 높이로 나누고 남은 나머지가 층수를 결정. 만약 0이면 맨 꼭대기층.
# 호수 (N//H)+1: N번째 손님 앞에 몇개의 H들이 쌓인 것에 따라 결정. 즉, N을 H로 나눈 몫 +1이 호수가 됨
n = int(input())
for i in range(0,n):
  H, W, N = map(int, input().split())
  if N%H==0:
    print(H*100 +N//H)
  else:
    print(N%H*100 + (N//H)+1)