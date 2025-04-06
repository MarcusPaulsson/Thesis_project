def solve():
    s = input()
    n = len(s)
    t = ""
    u = ""
    
    suffix_min = [""] * (n + 1)
    suffix_min[n] = ""
    
    for i in range(n - 1, -1, -1):
        if suffix_min[i+1] == "" or s[i] < suffix_min[i+1][0]:
            suffix_min[i] = s[i]
        else:
            suffix_min[i] = suffix_min[i+1][0]
        suffix_min[i] += suffix_min[i+1]
    
    i = 0
    while i < n:
        if len(t) == 0:
            t += s[i]
            i += 1
        elif suffix_min[i] == "" or t[-1] <= suffix_min[i][0]:
            u += t[-1]
            t = t[:-1]
        else:
            t += s[i]
            i += 1
            
    while len(t) > 0:
        u += t[-1]
        t = t[:-1]
        
    print(u)

solve()