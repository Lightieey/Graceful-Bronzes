A, B, C = map(int, input().split())
if C <= B:
   # N이 지속적 증가했을 때 영향 받는 것은 C와 B, 
   # B(가변비용)이 C(판매비용) 보다 크거나 같으면 이익이 없어 손익분기점을 넘길 수 없음
  print("-1")
else:
  # 위의 경우를 제외하면 손익분기점을 넘김
  # 그때의 N개 개수를 구하는 것은 위의 CxN > A + BxN을 정리하여 N > A//(C-B) 인데
  # A//(C-B) 에서 1을 더해야 N이 됨
  print((A//(C-B))+1)