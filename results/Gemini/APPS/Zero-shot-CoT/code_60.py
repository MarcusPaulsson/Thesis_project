def solve():
    a, b = map(int, input().split())
    print(a ^ b)

t = int(input())
for _ in range(t):
    solve()