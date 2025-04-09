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
        
        for digit in sorted(list(set(remaining_digits)), reverse=True):
            temp_remaining_digits = remaining_digits[:]
            temp_remaining_digits.remove(digit)
            new_num = current_num + digit
            
            if new_num <= b[:index+1]:
                if new_num == b[:index+1]:
                    result = find_max_permutation(index + 1, new_num, temp_remaining_digits)
                    if result != "" and (best_num == "" or result > best_num):
                        best_num = result
                else:
                    sorted_remaining = sorted(temp_remaining_digits, reverse=True)
                    result = new_num + "".join(sorted_remaining)
                    if best_num == "" or result > best_num:
                        best_num = result
        return best_num
    
    result = find_max_permutation(0, "", list(a))
    print(result)

solve()