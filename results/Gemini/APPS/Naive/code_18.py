def solve():
    s = input()
    n = len(s)
    
    u = ""
    t = ""
    
    suffix_min = [0] * n
    suffix_min[-1] = s[-1]
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(s[i], suffix_min[i+1])
    
    
    i = 0
    while i < n:
        if not t:
            t += s[i]
            i += 1
        elif i < n and suffix_min[i] < t[-1]:
            t += s[i]
            i += 1
        else:
            u += t[-1]
            t = t[:-1]
    
    while t:
        u += t[-1]
        t = t[:-1]
        
    print(u)

solve()