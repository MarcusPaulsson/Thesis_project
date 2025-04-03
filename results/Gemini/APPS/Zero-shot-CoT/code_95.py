def solve():
    n = int(input())
    if n == 1:
        print("-1")
        return
    
    s = ""
    for i in range(n):
        s += "2"
    print(s)

t = int(input())
for _ in range(t):
    solve()