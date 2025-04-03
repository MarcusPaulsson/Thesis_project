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
    
    
    
    def get_string(removed_indices):
        temp_s_list = s_list[:]
        removed_indices = sorted(removed_indices, reverse=True)
        for index in removed_indices:
            del temp_s_list[index]
        return "".join(temp_s_list)

    
    import itertools
    
    cleanest_string = s
    
    for r in range(len(indices_to_remove) + 1):
        for combination in itertools.combinations(indices_to_remove, r):
            
            
            temp_s_list = s_list[:]
            removed_indices = []
            
            
            for index in combination:
                
                if index+1 < len(temp_s_list) and temp_s_list[index] == '1' and temp_s_list[index+1] == '0':
                    removed_indices.append(index)
                elif index-1 >=0 and temp_s_list[index-1] == '1' and temp_s_list[index] == '0':
                    removed_indices.append(index)
                
            
            
            
            string_1 = ""
            string_2 = ""
            
            
            
            temp_s_list_1 = s_list[:]
            
            
            
            removed_indices_1 = []
            
            
            for index in combination:
                
                if index+1 < len(temp_s_list_1) and temp_s_list_1[index] == '1' and temp_s_list_1[index+1] == '0':
                    removed_indices_1.append(index)
                
                
            
            string_1 = get_string(removed_indices_1)
            
            
            
            temp_s_list_2 = s_list[:]
            removed_indices_2 = []
            
            
            for index in combination:
                
                valid = False
                
                if index+1 < len(s_list) and s_list[index] == '1' and s_list[index+1] == '0':
                    valid = True
                
                
                
                if index-1 >=0 and s_list[index-1] == '1' and s_list[index] == '0':
                    valid = True
                
                
                if valid:
                    
                    
                    if index+1 < len(temp_s_list_2) and temp_s_list_2[index] == '1' and temp_s_list_2[index+1] == '0':
                        removed_indices_2.append(index+1)
                    elif index-1 >=0 and temp_s_list_2[index-1] == '1' and temp_s_list_2[index] == '0':
                        removed_indices_2.append(index)
            
            
            string_2 = get_string(removed_indices_2)
            
            
            
            
            current_string = min(string_1, string_2)
            
            
            
            if len(current_string) < len(cleanest_string):
                cleanest_string = current_string
            elif len(current_string) == len(cleanest_string) and current_string < cleanest_string:
                cleanest_string = current_string
            
            
    print(cleanest_string)
    

t = int(input())
for _ in range(t):
    solve()