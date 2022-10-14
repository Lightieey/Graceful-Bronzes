#구글링 활용함.
#앞의 2750의 코드를 import sys 사용하여 시간 단축함.

import sys
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(sys.stdin.readline()))
for i in sorted(numbers):
    sys.stdout.write(str(i)+'\n')