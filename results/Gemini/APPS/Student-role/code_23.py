from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    
    if len(a) < len(b):
        print("".join(a_digits))
        return
    
    if len(a) > len(b):
        
        print("".join(a_digits))
        return

    
    def find_max_permutation(index, current_num, remaining_digits):
        if index == len(a):
            return current_num
        
        best_num = ""
        
        for digit in sorted(remaining_digits.keys(), reverse=True):
            if remaining_digits[digit] > 0:
                
                temp_remaining_digits = remaining_digits.copy()
                temp_remaining_digits[digit] -= 1
                if temp_remaining_digits[digit] == 0:
                    del temp_remaining_digits[digit]
                    
                new_num = current_num + digit
                
                if int(new_num) <= int(b[:index+1]):
                    
                    if int(new_num) == int(b[:index+1]):
                        
                        result = find_max_permutation(index + 1, new_num, temp_remaining_digits)
                        if result != "" and (best_num == "" or int(result) > int(best_num)):
                            best_num = result
                    else:
                        
                        remaining_digits_list = []
                        for d, count in temp_remaining_digits.items():
                            remaining_digits_list.extend([d] * count)
                        remaining_digits_list.sort(reverse=True)
                        
                        
                        full_num = new_num + "".join(remaining_digits_list)
                        if best_num == "" or int(full_num) > int(best_num):
                            best_num = full_num
        
        return best_num
    
    a_counts = Counter(a)
    result = find_max_permutation(0, "", a_counts)
    print(result)

solve()