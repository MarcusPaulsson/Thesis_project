def solve():
    s = input()
    n = len(s)
    t = []
    u = ""
    
    min_suffix = [0] * (n + 1)
    min_suffix[n] = 'z'  # Initialize with a large value
    for i in range(n - 1, -1, -1):
        min_suffix[i] = min(s[i], min_suffix[i+1])
    
    i = 0
    while i < n:
        if len(t) > 0 and t[-1] <= min_suffix[i]:
            u += t[-1]
            t.pop()
        else:
            t.append(s[i])
            i += 1
            
    while len(t) > 0:
        u += t[-1]
        t.pop()
        
    print(u)

solve()