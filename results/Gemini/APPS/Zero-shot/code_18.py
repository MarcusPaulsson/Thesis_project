def solve():
    s = input()
    n = len(s)
    t = ""
    u = ""
    
    suffix_min = [0] * (n + 1)
    suffix_min[n] = 'z'
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(s[i], suffix_min[i+1])
    
    i = 0
    while i < n or len(t) > 0:
        if i < n and (len(t) == 0 or suffix_min[i] <= t[-1]):
            t += s[i]
            i += 1
        else:
            u += t[-1]
            t = t[:-1]
            
    print(u)

solve()