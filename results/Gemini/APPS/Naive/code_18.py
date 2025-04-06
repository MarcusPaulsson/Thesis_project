def solve():
    s = input()
    n = len(s)
    t = []
    u = ""
    
    min_suffixes = [""] * (n + 1)
    min_suffixes[n] = ""
    
    for i in range(n - 1, -1, -1):
        if min_suffixes[i + 1] == "" or s[i] < min_suffixes[i + 1][0]:
            min_suffixes[i] = s[i]
        elif s[i] == min_suffixes[i + 1][0]:
            min_suffixes[i] = s[i] + min_suffixes[i + 1]
        else:
            min_suffixes[i] = min_suffixes[i + 1]
    
    min_suffixes[0] = s[0] + min_suffixes[1]

    
    for i in range(n):
        if not s:
            while t:
                u += t.pop()
            break
        
        if not t:
            t.append(s[0])
            s = s[1:]
        else:
            if s[0] <= min_suffixes[len(s)]:
                t.append(s[0])
                s = s[1:]
            else:
                while t and t[-1] <= min_suffixes[len(s)][0]:
                    u += t.pop()
                if not t or s[0] <= t[-1]:
                  t.append(s[0])
                  s = s[1:]
                else:
                  u += t.pop()
    while t:
        u += t.pop()
    print(u)

solve()