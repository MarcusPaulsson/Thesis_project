def solve():
    n = int(input())
    s = input()
    
    g_count = s.count('G')
    
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            
            subsegment = s[i:j+1]
            
            if all(c == 'G' for c in subsegment):
                max_len = max(max_len, len(subsegment))
                
    
    ans = 0
    for i in range(n):
        for j in range(n):
            temp_s = list(s)
            temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
            temp_s = "".join(temp_s)
            
            curr_max = 0
            curr_len = 0
            for k in range(n):
                if temp_s[k] == 'G':
                    curr_len += 1
                else:
                    curr_max = max(curr_max, curr_len)
                    curr_len = 0
            curr_max = max(curr_max, curr_len)
            ans = max(ans, curr_max)
    
    
    max_len = 0
    for i in range(n):
        curr_len = 0
        for j in range(i, n):
            if s[j] == 'G':
                curr_len += 1
            else:
                break
        max_len = max(max_len, curr_len)
    
    initial_max_len = max_len
    
    ans = 0
    for i in range(n):
        if s[i] == 'S':
            temp_s = list(s)
            
            
            
            
            
            
            
            
            g_indices = [idx for idx, val in enumerate(s) if val == 'G']
            
            if not g_indices:
                continue
            
            
            for g_index in g_indices:
              temp_s = list(s)
              temp_s[i], temp_s[g_index] = temp_s[g_index], temp_s[i]
              temp_s = "".join(temp_s)
              
              curr_max = 0
              curr_len = 0
              for k in range(n):
                  if temp_s[k] == 'G':
                      curr_len += 1
                  else:
                      curr_max = max(curr_max, curr_len)
                      curr_len = 0
              curr_max = max(curr_max, curr_len)
              ans = max(ans, curr_max)
    
    
    
    if s.count('G') == 0:
        print(0)
        return
        
    
    max_len = 0
    for i in range(n):
        curr_len = 0
        for j in range(i, n):
            if s[j] == 'G':
                curr_len += 1
            else:
                break
        max_len = max(max_len, curr_len)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    max_len_after_swap = 0
    for i in range(n):
        if s[i] == 'S':
            for j in range(n):
                if s[j] == 'G':
                    temp_s = list(s)
                    temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
                    temp_s = "".join(temp_s)
                    
                    curr_max = 0
                    curr_len = 0
                    for k in range(n):
                        if temp_s[k] == 'G':
                            curr_len += 1
                        else:
                            curr_max = max(curr_max, curr_len)
                            curr_len = 0
                    curr_max = max(curr_max, curr_len)
                    max_len_after_swap = max(max_len_after_swap, curr_max)
    
    if max_len_after_swap == 0 and s.count('G') > 0:
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        
        segments = []
        curr_len = 0
        for char in s:
            if char == 'G':
                curr_len += 1
            else:
                if curr_len > 0:
                    segments.append(curr_len)
                curr_len = 0
        if curr_len > 0:
            segments.append(curr_len)
            
        if not segments:
          print(0)
          return
          
        if len(segments) == 1:
          print(min(segments[0] + 1, g_count))
          return
        max_len_possible = 0
        for i in range(len(segments) - 1):
          max_len_possible = max(max_len_possible, segments[i] + segments[i+1] + 1)
        
        
        curr_max = 0
        curr_len = 0
        for k in range(n):
            if s[k] == 'G':
                curr_len += 1
            else:
                curr_max = max(curr_max, curr_len)
                curr_len = 0
        curr_max = max(curr_max, curr_len)
        
        print(min(curr_max + 1, g_count))
        return
    
    
    if s.count('S') == 0:
        print(n)
        return
    
    
    
    
    
    
    
    
    
    print(max(ans, max_len_after_swap))
    
solve()