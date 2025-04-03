def solve():
    n = int(input())
    if n == 1:
        print("-1")
    else:
        s = ""
        for _ in range(n):
            s += "2"
        print(s)

t = int(input())
for _ in range(t):
    solve()