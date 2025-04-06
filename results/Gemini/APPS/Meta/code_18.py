def solve():
    s = input()
    n = len(s)
    t = []
    u = ""
    
    suffix_min = [""] * (n + 1)
    suffix_min[n] = chr(ord('z') + 1) 
    
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(s[i], suffix_min[i+1])
    
    i = 0
    while i < n or t:
        if not t:
            if s[i] <= suffix_min[i+1]:
                u += s[i]
                i += 1
            else:
                t.append(s[i])
                i += 1
        else:
            if i < n and suffix_min[i+1] < t[-1]:
                if s[i] <= suffix_min[i+1]:
                    u += s[i]
                    i += 1
                else:
                    t.append(s[i])
                    i += 1
            else:
                u += t.pop()
    
    print(u)

solve()