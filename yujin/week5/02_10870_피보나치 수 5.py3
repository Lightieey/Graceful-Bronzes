def fivo(n):
  if n <= 1:
    # 1일 때 아래 else문으로 넘어가면 -1 0 으로 호출되니까 그거 방지
    return n
  else:
    return fivo(n-2)+fivo(n-1)
print(fivo(int(input())))