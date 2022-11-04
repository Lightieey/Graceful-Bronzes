N = int(input())
li =[]
n_666=True
stop = False
count = 0
order=0
i=0
while True:
  i+=1
  num = str(i)
  for n in num:
    # 각자리 수 보면서 연속으로 6이 3번 나오는지 체크
    if n=="6":
      n_666==True
      if n_666:
        count+=1
      if count ==3:
        order+=1
        if order==N:
          #print(count, order)
          print(i)
          stop=True
          break
    elif n!="6":
      n_666==False
      count=0
  if stop:
    break
  count=0

