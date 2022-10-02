# 단어 공부
# count
import sys

spelling = sys.stdin.readline()

# Mississipi
alphabet = []
for i in spelling:
    if i.upper() not in alphabet:
        alphabet.append(i.upper())

alphabet.remove('\n')
# alphabet = [M,I,S,P]
countList = []
count = 0

for i in alphabet:
    for j in spelling:
        if j.upper() == i:
            count += 1
    countList.append(count)
    count = 0

# countList = [ 1, 4, 4, 1]
same = 0
for c in countList:
    if c == max(countList):
        same += 1

if same > 1:
    print('?')
else:
    maxIndex = countList.index(max(countList))
    print(alphabet[maxIndex])




