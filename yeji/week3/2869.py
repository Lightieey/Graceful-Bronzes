# 시간초과...
#
# A, B, Z = map(int, input().split())
# now = 0
# cnt = 0
#
# while True:
#     now += A
#     if now >= Z:
#         print(cnt+1)
#         break
#     else:
#         now -= B
#         if now >= Z:
#             print(cnt)
#             break
#         else:
#             cnt +=1
#


A,B,V = map(int, input().split())

if (V-B) % (A-B) == 0 :
    print((V-B) // (A-B))
else :
    print(((V-B) // (A-B)) +1)