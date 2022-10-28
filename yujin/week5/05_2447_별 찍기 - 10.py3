n = int(input())

def star(l):
  if l == 3:
    # 3이면 그려줄 패턴
    return ['***','* *','***']
  # 3보다 클 경우 3으로 나눈 것을 넘겨서 패턴 얻어옴
  arr = star(l//3) 
  stars = []
  # 만약 l이 9여서 위게서 arr에 3패턴 얻어왔으면
  for i in arr:
    # 일단 첫줄은 3번 그려
    stars.append(i*3)

  for i in arr:
    # 두번째 줄은 중간 부분은 l을 3으로 나눈 만큼 비워줘야 함
    # 양 끝은 동일하게 가져온 패턴 붙이기
    stars.append(i+' '*(l//3)+i)

  for i in arr:
    # 세번째 줄도 3번 그려
    stars.append(i*3)

  return stars

print('\n'.join(star(n)))