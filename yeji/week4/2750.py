N = int(input())
numbers = []
for i in range(0, N):
    a = int(input())
    numbers.append(a) #숫자 받아서 리스트로 저장


numbers.sort() #오름차순으로 정렬
for r in range(0, N):
    print(numbers[r], end="\n")  #한줄씩 숫자 출력