def greatest_integer(n):
    if n % 2 == 0:
        return '1' * (n // 2)
    else:
        return '7' + '1' * (n // 2 - 1)

t = int(input())
for _ in range(t):
    n = int(input())
    print(greatest_integer(n))