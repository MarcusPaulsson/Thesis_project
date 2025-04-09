def solve():
    s = input()
    n = len(s)
    t = ""
    u = ""
    
    suffix_min = [""] * (n + 1)
    suffix_min[n] = chr(127)  # Initialize with a character larger than 'z'
    
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(s[i], suffix_min[i+1])
    
    i = 0
    while i < n:
        if t == "" or suffix_min[i] <= t[-1]:
            t += s[i]
            i += 1
        else:
            u += t[-1]
            t = t[:-1]
            
    while t != "":
        u += t[-1]
        t = t[:-1]
    
    print(u)

solve()