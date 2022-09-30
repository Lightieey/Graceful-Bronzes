voca = input().upper()
alphabet_set = set(voca)
alphabet_list=[]
for a in alphabet_set:
  alphabet_list.append([a, voca.count(a)])
alphabet_list.sort(key=lambda x: x[1], reverse=True)
if len(voca)==1:
  print(voca)
elif alphabet_list[0][1] == alphabet_list[1][1]:
  print("?")
else:
  print(alphabet_list[0][0])