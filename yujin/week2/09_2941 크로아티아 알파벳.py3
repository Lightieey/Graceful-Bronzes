croatia = ["c=", "c-","dz=", "d-", "lj", "nj", "s=", "z="]
voca = input()
count = 0
while True:
  if len(voca) ==0:
    break
  elif voca[0: 2] in croatia:
    count+=1
    voca = voca[2: ]
  elif voca[0:3] in croatia:
    count+=1
    voca = voca[3: ]
  else:
    count+=1
    voca =voca[1: ]
  
print(count)
