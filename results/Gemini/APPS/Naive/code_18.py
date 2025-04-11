def solve():
    s = input()
    n = len(s)
    
    suffix_min = [0] * (n + 1)
    suffix_min[n] = 'z'
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(s[i], suffix_min[i+1])
    
    t = []
    u = ""
    
    for i in range(n):
        t.append(s[i])
        while t and t[-1] <= suffix_min[i+1]:
            u += t.pop()
            
    while t:
        u += t.pop()
        
    print(u)

solve()