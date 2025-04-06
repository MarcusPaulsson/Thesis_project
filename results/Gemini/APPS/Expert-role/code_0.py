def solve():
    s = input()
    n = len(s)
    
    max_len = -1
    
    for i in range(n):
        if s[i] == '[':
            for j in range(i + 1, n):
                if s[j] == ':':
                    for k in range(j + 1, n):
                        for l in range(k + 1, n):
                            if s[l] == ']':
                                if s[k] == ':':
                                    
                                    num_pipes = 0
                                    for m in range(j + 1, k):
                                        if s[m] == '|':
                                            num_pipes += 1
                                    
                                    current_len = 2 + 2 + num_pipes
                                    max_len = max(max_len, current_len)
    
    print(max_len)

solve()