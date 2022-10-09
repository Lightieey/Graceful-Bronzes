import sys
#N = input()
N = sys.stdin.readline()
num_list = []
for n in N:
  num_list.append(n)
num_list.sort(reverse=True)
print("".join(num_list)) # 리스트 문자열로 합침 