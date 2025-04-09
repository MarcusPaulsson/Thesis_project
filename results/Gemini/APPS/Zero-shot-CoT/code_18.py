def solve():
    s = input()
    n = len(s)
    t = []
    u = []
    
    min_suffix = [''] * (n + 1)
    min_suffix[n] = chr(123) 
    
    for i in range(n - 1, -1, -1):
        min_suffix[i] = min(s[i], min_suffix[i+1])
    
    i = 0
    while i < n:
        if len(t) == 0:
            t.append(s[i])
            i += 1
        elif min_suffix[i] < t[-1]:
            t.append(s[i])
            i += 1
        else:
            u.append(t.pop())
    
    while len(t) > 0:
        u.append(t.pop())
        
    print("".join(u))

solve()