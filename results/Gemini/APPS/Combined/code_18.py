def solve():
    s = input()
    n = len(s)
    
    suffix_min = [0] * (n + 1)
    suffix_min[n] = chr(ord('z') + 1)  # Initialize with a value greater than 'z'
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(s[i], suffix_min[i+1])
    
    t = []
    u = ""
    
    for i in range(n):
        t.append(s[i])
        while t and t[-1] <= suffix_min[i+1]:
            u += t[-1]
            t.pop()
            
    while t:
        u += t[-1]
        t.pop()
        
    print(u)

solve()