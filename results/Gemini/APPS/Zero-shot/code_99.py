def solve():
    n = int(input())
    s = input()
    
    s_list = list(s)
    
    indices_to_remove = []
    
    i = 0
    while i < len(s_list) - 1:
        if s_list[i] == '1' and s_list[i+1] == '0':
            indices_to_remove.append(i)
            i += 2
        else:
            i += 1
            
    
    
    
    
    import itertools
    
    best_string = s
    
    
    
    for r in range(len(indices_to_remove)+1):
        for comb in itertools.combinations(indices_to_remove, r):
            temp_s_list = list(s)
            temp_indices_to_remove = list(comb)
            
            temp_indices_to_remove.sort(reverse=True)
            
            
            
            
            
            
            current_s_list = list(s)
            
            removed_count = 0
            
            
            for index in temp_indices_to_remove:
                
                
                
                if index - removed_count >= 0 and index - removed_count + 1 < len(current_s_list) and current_s_list[index - removed_count] == '1' and current_s_list[index - removed_count + 1] == '0':
                    
                    
                    
                    
                    
                    
                    current_s_list.pop(index - removed_count + 1)
                    
                    removed_count += 1
                    
                    
                
                
                    
            
            
            
            current_s = "".join(current_s_list)
            
            
            
            
            
            
            
            
            if len(current_s) < len(best_string):
                
                best_string = current_s
            elif len(current_s) == len(best_string):
                
                if current_s < best_string:
                    
                    best_string = current_s
    
    print(best_string)

t = int(input())
for _ in range(t):
    solve()