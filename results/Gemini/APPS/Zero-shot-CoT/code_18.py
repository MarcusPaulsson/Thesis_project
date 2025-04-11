def solve():
    s = input()
    n = len(s)
    t = ""
    u = ""
    
    min_suffix = [""] * (n + 1)
    min_suffix[n] = ""
    for i in range(n - 1, -1, -1):
        if min_suffix[i+1] == "":
            min_suffix[i] = s[i]
        else:
            if s[i] <= min_suffix[i+1][0]:
                min_suffix[i] = s[i] + min_suffix[i+1]
            else:
                min_suffix[i] = min_suffix[i+1]
    
    for i in range(n):
        t += s[0]
        s = s[1:]
        
        while len(t) > 0 and t[-1] <= min_suffix[i+1][0] if i+1 < n else len(t) > 0:
            u += t[-1]
            t = t[:-1]
    
    u += t[::-1]
    print(u)
    

solve()