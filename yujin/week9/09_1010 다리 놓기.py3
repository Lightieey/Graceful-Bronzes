import math
T = int(input())
for i in range(T):
  N, K = map(int, input().split())
  if 0<=K and K <=N:
    print(math.comb(N, K))
  elif K <0 or K>N:
    print(math.comb(K, N))
