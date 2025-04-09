def solve():
    n = int(input())
    s = input()
    
    g_count = s.count('G')
    
    max_len = 0
    
    for i in range(n):
        if s[i] == 'S':
            for j in range(n):
                if s[j] == 'G':
                    temp_s = list(s)
                    temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
                    
                    current_len = 0
                    max_current_len = 0
                    
                    for char in temp_s:
                        if char == 'G':
                            current_len += 1
                        else:
                            max_current_len = max(max_current_len, current_len)
                            current_len = 0
                    max_current_len = max(max_current_len, current_len)
                    
                    max_len = max(max_len, min(max_current_len, g_count))
    
    current_len = 0
    max_initial_len = 0
    for char in s:
        if char == 'G':
            current_len += 1
        else:
            max_initial_len = max(max_initial_len, current_len)
            current_len = 0
    max_initial_len = max(max_initial_len, current_len)
    
    print(max(min(max_initial_len, g_count), max_len))

solve()