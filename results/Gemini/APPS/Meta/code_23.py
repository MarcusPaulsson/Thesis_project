def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    
    if len(a) < len(b):
        print("".join(a_digits))
        return
    
    def find_max_permutation(index, current_num, remaining_digits):
        if index == len(a):
            return current_num
        
        best_num = ""
        
        for i in range(len(remaining_digits)):
            digit = remaining_digits[i]
            
            if int(current_num + digit) <= int(b[:index+1]):
                new_num = current_num + digit
                new_remaining = remaining_digits[:i] + remaining_digits[i+1:]
                
                if int(new_num) > int(b[:index+1]):
                    continue
                
                result = find_max_permutation(index + 1, new_num, new_remaining)
                
                if result != "" and (best_num == "" or int(result) > int(best_num)):
                    best_num = result
        
        return best_num

    import collections
    a_counts = collections.Counter(a)
    
    
    if len(a) > len(b):
        print("".join(sorted(a, reverse=True)))
        return
    
    
    
    
    def find_permutation(index, current_num, remaining_counts):
        if index == len(a):
            return current_num
        
        best_num = ""
        
        for digit in sorted(remaining_counts.keys(), reverse=True):
            if remaining_counts[digit] > 0:
                new_num = current_num + digit
                
                if int(new_num) <= int(b[:index+1]):
                    new_counts = remaining_counts.copy()
                    new_counts[digit] -= 1
                    if new_counts[digit] == 0:
                        del new_counts[digit]
                    
                    result = find_permutation(index + 1, new_num, new_counts)
                    
                    if result != "" and (best_num == "" or int(result) > int(best_num)):
                        best_num = result
        
        return best_num

    
    a_counts = collections.Counter(a)
    result = find_permutation(0, "", a_counts)
    
    print(result)
    

solve()