voca = input()
alphabet_dict = {}
for s in voca:
  if alphabet_dict.get(ord(s)) == None:
    # 키값이 존재하지 않을 경우 해당 알파벳에 시작 위치 인덱스 넣어주기
    alphabet_dict[ord(s)] = voca.find(s) 

alphabet_find_list = []  
for i in range(ord("a"), ord("z")+1):
  #if alphabet_dict.get(i):
  if i in alphabet_dict:
    # key값이 존재하면 value 가져와서 인덱스 위치 넣기
    alphabet_find_list.append(alphabet_dict[i])
  else:
    # 존재하지 않는 경우 -1
    alphabet_find_list.append(-1)
#print(alphabet_find_list) # 문제에서 공백^^으로 구분하라 함
for a in alphabet_find_list:
  print(a, end=" ")