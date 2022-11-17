# 서로 다른 부분 문자열의 개수

S = input()

i = 1
S_str = set()
while i <= len(S):
    temp = S
    while temp:
        S_str.add(temp[0:i])
        temp = temp[1:]
    i += 1

print(len(S_str))

