def solve():
    s = input()
    n = len(s)
    
    max_len = -1
    
    for i in range(n):
        for j in range(i + 3, n):
            
            sub = ""
            
            
            first_bracket_index = -1
            for k in range(n):
                if s[k] == '[':
                    first_bracket_index = k
                    break
                    
            last_bracket_index = -1
            for k in range(n-1, -1, -1):
                if s[k] == ']':
                    last_bracket_index = k
                    break
                    
            if first_bracket_index == -1 or last_bracket_index == -1 or first_bracket_index >= last_bracket_index:
                continue
            
            
            first_colon_index = -1
            for k in range(first_bracket_index + 1, n):
                if s[k] == ':':
                    first_colon_index = k
                    break
                    
            last_colon_index = -1
            for k in range(last_bracket_index - 1, -1, -1):
                if s[k] == ':':
                    last_colon_index = k
                    break
            
            
            if first_colon_index == -1 or last_colon_index == -1 or first_colon_index >= last_colon_index:
                continue
                
            
            
            num_pipes = 0
            for k in range(first_colon_index + 1, last_colon_index):
                if s[k] == '|':
                    num_pipes += 1
                    
            
            curr_len = 4 + num_pipes
            
            if curr_len > max_len and first_bracket_index < first_colon_index and first_colon_index < last_colon_index and last_colon_index < last_bracket_index:
                max_len = curr_len

    print(max_len)

solve()