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
            
            temp_num = current_num + digit
            
            if int(temp_num) > int(b[:index+1]):
                continue
            
            new_remaining_digits = remaining_digits[:i] + remaining_digits[i+1:]
            
            if int(temp_num) == int(b[:index+1]):
                next_num = find_max_permutation(index + 1, temp_num, new_remaining_digits)
                if next_num != "" and (best_num == "" or int(next_num) > int(best_num)):
                    best_num = next_num
            else:
                temp_num += "".join(sorted(new_remaining_digits, reverse=True))
                if best_num == "" or int(temp_num) > int(best_num):
                    best_num = temp_num
        
        return best_num
    
    result = find_max_permutation(0, "", a_digits)
    print(result)

solve()