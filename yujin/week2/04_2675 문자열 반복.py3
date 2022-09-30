test_case_num = int(input())
for i in range(0, test_case_num):
  repeat_num, voca = map(str, input().split())
  for v in voca:
    for i in range(0, int(repeat_num)):
      print(v, end="")
  print("")
    