def solve():
    s = input()
    n = len(s)
    
    max_len = -1
    
    for i in range(n):
        if s[i] == '[':
            for j in range(i + 1, n):
                if s[j] == ':':
                    for k in range(j + 1, n):
                        if s[k] == ':':
                            for l in range(k + 1, n):
                                if s[l] == ']':
                                    
                                    valid = True
                                    for m in range(i + 1, j):
                                        if s[m] != '|':
                                            valid = False
                                            break
                                    
                                    for m in range(j + 1, k):
                                        if s[m] != '|':
                                            valid = False
                                            break
                                    
                                    if valid:
                                        length = 4 + (k - j - 1) + (j - i - 1)
                                        max_len = max(max_len, length)
    
    print(max_len)

solve()