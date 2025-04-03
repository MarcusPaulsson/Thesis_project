def solve():
    s = input()
    t = input()
    n = len(s)
    
    s_chars = set(s)
    t_chars = set(t)
    
    if any(c in s_chars for c in t_chars):
        print("YES")
    else:
        print("NO")

q = int(input())
for _ in range(q):
    solve()