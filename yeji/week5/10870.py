def sum(n):
    if n <= 1:
        return n
    return sum(n-1) + sum(n-2)

n = int(input())
print(sum(n))