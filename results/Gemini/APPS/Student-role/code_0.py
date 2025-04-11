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
                                    
                                    count = 0
                                    for m in range(k + 1, l):
                                        if s[m] == '|':
                                            count += 1
                                    
                                    curr_len = 2 + 2 + count
                                    
                                    max_len = max(max_len, curr_len)
    
    print(max_len)

solve()