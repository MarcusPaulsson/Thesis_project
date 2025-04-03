def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*a)
    print(*b)

t = int(input())
for _ in range(t):
    solve()