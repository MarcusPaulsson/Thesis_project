def solve():
    s = input()
    n = len(s)
    t = []
    u = ""
    
    suffix_min = [""] * (n + 1)
    suffix_min[n] = chr(ord('z') + 1)
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(s[i], suffix_min[i+1])
    
    for i in range(n):
        while t and t[-1] <= suffix_min[i]:
            u += t.pop()
        t.append(s[i])
        
    while t:
        u += t.pop()
        
    print(u)

solve()