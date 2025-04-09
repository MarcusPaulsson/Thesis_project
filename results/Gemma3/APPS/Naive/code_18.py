def solve():
    s = input()
    t = ""
    u = ""
    
    while s:
        t += s[0]
        s = s[1:]
        
        if s:
            u += t[-1]
            t = t[:-1]
            
    while t:
        u += t[-1]
        t = t[:-1]
        
    print(u)

solve()