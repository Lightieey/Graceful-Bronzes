h, m = map(int, input().split())
time = int(input())

all_time = h*60 + m + time
final_h = all_time//60
final_m = all_time%60

if final_h >23:
  final_h = final_h-24
print(final_h, final_m)
