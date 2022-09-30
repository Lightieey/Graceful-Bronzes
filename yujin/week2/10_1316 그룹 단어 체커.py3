
def isGroupVoca(voca):
  vcount=0
  judgment = []
  for v in voca:
    if vcount==0:
      judgment.append(v)
      vcount +=1
    elif (judgment[vcount-1] == v):
      # aa
      pass
    elif not(v in judgment) and not(judgment[vcount-1] == v):
      # aap
      judgment.append(v)
      vcount +=1
    elif (v in judgment) and not(judgment[vcount-1] == v):
      vcount = -1
      break
  if vcount == -1:
    return False
  else:
    return True
  

num = int(input())
group =0
for i in range(0, num):
  voca = input()
  if isGroupVoca(voca):
    group+=1
print(group)