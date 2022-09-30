voca = input()
time=3
dial={}
time_up = [67, 70, 73, 76, 79,83,86,90]
for v in range(65, 91):
  dial[v] = time
  if v in time_up:
    time+=1
time = 0
for v in voca:
  v_ascii = ord(v)
  time += dial[v_ascii]
print(time)