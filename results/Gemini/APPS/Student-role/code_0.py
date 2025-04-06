def solve():
    s = input()
    n = len(s)
    
    max_len = -1
    
    for i in range(n):
        if s[i] == '[':
            for j in range(i + 1, n):
                if s[j] == ':':
                    for k in range(j + 1, n):
                        for l in range(k, n):
                            if s[l] == ':':
                                for m in range(l + 1, n):
                                    if s[m] == ']':
                                        
                                        count = 0
                                        for p in range(k + 1, l):
                                            if s[p] == '|':
                                                count += 1
                                        
                                        curr_len = 4 + count
                                        max_len = max(max_len, curr_len)
    
    print(max_len)

solve()