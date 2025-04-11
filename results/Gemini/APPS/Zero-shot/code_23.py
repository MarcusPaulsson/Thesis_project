def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    
    if len(a) < len(b):
        print("".join(a_digits))
        return
    
    def find_max(index, current_num, remaining_digits):
        if index == len(a):
            return current_num
        
        best_num = ""
        
        for i in range(len(remaining_digits)):
            digit = remaining_digits[i]
            
            if current_num == "" and digit == '0':
                continue
            
            new_num = current_num + digit
            
            if int(new_num) <= int(b[:len(new_num)]):
                
                remaining_digits_copy = remaining_digits[:i] + remaining_digits[i+1:]
                
                if len(new_num) == len(b):
                    
                    temp_num = new_num + "".join(sorted(remaining_digits_copy, reverse=True))
                    
                    if int(temp_num) <= int(b):
                        if best_num == "" or int(temp_num) > int(best_num):
                            best_num = temp_num
                else:
                    
                    res = find_max(index + 1, new_num, remaining_digits_copy)
                    if res != "":
                        if best_num == "" or int(res) > int(best_num):
                            best_num = res
        
        return best_num
    
    result = find_max(0, "", a_digits)
    print(result)

solve()