def solve():
    s = input()
    n = len(s)
    
    max_len = -1
    
    for i in range(n):
        if s[i] == '[':
            for j in range(i + 1, n):
                if s[j] == ']':
                    for k in range(i + 1, j):
                        if s[k] == ':':
                            for l in range(k + 1, j):
                                if s[l] == ':':
                                    
                                    
                                    vertical_bars = 0
                                    for m in range(k + 1, l):
                                        if s[m] == '|':
                                            vertical_bars += 1
                                    
                                    current_len = 4 + vertical_bars
                                    max_len = max(max_len, current_len)
    
    print(max_len)

solve()