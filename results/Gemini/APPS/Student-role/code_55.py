def solve():
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    elif n % 2 == 0:
        print(n // 2)
    else:
        print((n + 1) // 2)

t = int(input())
for _ in range(t):
    solve()