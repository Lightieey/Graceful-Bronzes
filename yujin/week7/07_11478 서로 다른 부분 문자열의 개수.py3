S = input()
ret_set = set()
for i in range(0, len(S)):
  for j in range(i, len(S)):
    ret_set.add(S[i:j+1])
print(len(ret_set))