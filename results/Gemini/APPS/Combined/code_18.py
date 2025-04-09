def solve():
    s = input()
    n = len(s)
    
    min_suffix = [""] * (n + 1)
    min_suffix[n] = ""
    
    for i in range(n - 1, -1, -1):
        if min_suffix[i + 1] == "":
            min_suffix[i] = s[i]
        else:
            if s[i] <= min_suffix[i + 1][0]:
                min_suffix[i] = s[i] + min_suffix[i + 1]
            else:
                min_suffix[i] = min_suffix[i + 1]
                
    t = []
    u = ""
    
    for i in range(n):
        t.append(s[i])
        while t and (min_suffix[i+1] == "" or t[-1] <= min_suffix[i+1][0]):
            u += t.pop()
            
    while t:
        u += t.pop()
        
    print(u)

solve()