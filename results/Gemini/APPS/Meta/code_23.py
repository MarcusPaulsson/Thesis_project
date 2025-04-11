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
        
        max_num = ""
        
        for i in range(len(remaining_digits)):
            digit = remaining_digits[i]
            
            new_num = current_num + digit
            
            if int(new_num) <= int(b[:index+1]):
                new_remaining_digits = remaining_digits[:i] + remaining_digits[i+1:]
                
                if int(b[:index+1]) > int(new_num):
                    temp_digits = sorted(new_remaining_digits, reverse=True)
                    temp_num = new_num + "".join(temp_digits)
                    if len(max_num) == 0 or int(temp_num) > int(max_num):
                        max_num = temp_num
                else:
                    temp_num = find_max_permutation(index + 1, new_num, new_remaining_digits)
                    if len(temp_num) > 0 and (len(max_num) == 0 or int(temp_num) > int(max_num)):
                        max_num = temp_num
        
        return max_num
    
    result = find_max_permutation(0, "", a_digits)
    print(result)

solve()