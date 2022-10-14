#구글링 활용함.

n=int(input())
a=[]
for i in range(0,n):
    a.append(input())
a=list(set(a))      #중복제거
a.sort()            #알파벳 순으로 정렬
a.sort(key=len)     #길이 순으로 정렬

for i in a:
    print(i)