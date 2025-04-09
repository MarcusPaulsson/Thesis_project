def solve():
    s = input()
    n = len(s)
    
    max_len = -1
    
    for i in range(n):
        if s[i] == '[':
            for j in range(i + 1, n):
                if s[j] == ']':
                    
                    first_colon = -1
                    for k in range(i + 1, j):
                        if s[k] == ':':
                            first_colon = k
                            break
                    
                    if first_colon == -1:
                        continue
                    
                    second_colon = -1
                    for k in range(j - 1, first_colon, -1):
                        if s[k] == ':':
                            second_colon = k
                            break
                    
                    if second_colon == -1:
                        continue
                    
                    
                    pipes = 0
                    for k in range(first_colon + 1, second_colon):
                        if s[k] == '|':
                            pipes += 1
                    
                    current_len = 4 + pipes
                    max_len = max(max_len, current_len)
    
    print(max_len)

solve()