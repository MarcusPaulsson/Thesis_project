def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    b_digits = list(b)
    
    n_a = len(a)
    n_b = len(b)
    
    if n_a > n_b:
        print("".join(a_digits))
        return
    
    if n_a < n_b:
        print("".join(sorted(list(a), reverse=True)))
        return
    
    
    def find_max(idx, current_num, remaining_digits):
        if idx == n_a:
            return current_num
        
        best_num = None
        
        for i in range(len(remaining_digits)):
            digit = remaining_digits[i]
            
            if int(digit) > int(b_digits[idx]):
                continue
            
            new_remaining_digits = remaining_digits[:i] + remaining_digits[i+1:]
            
            new_num = current_num + digit
            
            if int(digit) < int(b_digits[idx]):
                
                sorted_remaining = sorted(new_remaining_digits, reverse=True)
                
                result = new_num + "".join(sorted_remaining)
                
                if best_num is None or int(result) > int(best_num):
                    best_num = result
            else:
                
                result = find_max(idx+1, new_num, new_remaining_digits)
                
                if result is not None:
                    if best_num is None or int(result) > int(best_num):
                        best_num = result
                        
        return best_num
    
    result = find_max(0, "", a_digits)
    print(result)
    
solve()