def solve():
    s = input()
    n = len(s)
    t = ""
    u = ""
    
    suffix_min = [""] * (n + 1)
    suffix_min[n] = chr(ord('z') + 1) 
    
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(s[i], suffix_min[i+1])
        
    
    while len(s) > 0:
        if s[0] <= suffix_min[0]:
            t += s[0]
            s = s[1:]
        else:
            while len(t) > 0 and t[-1] <= suffix_min[0]:
                u += t[-1]
                t = t[:-1]
            t += s[0]
            s = s[1:]
            
    while len(t) > 0:
        u += t[-1]
        t = t[:-1]
        
    print(u)

solve()