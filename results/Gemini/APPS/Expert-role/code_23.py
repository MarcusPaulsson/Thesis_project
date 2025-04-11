from collections import Counter

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
        
        for digit in sorted(remaining_digits.keys(), reverse=True):
            if remaining_digits[digit] > 0:
                temp_remaining_digits = remaining_digits.copy()
                temp_remaining_digits[digit] -= 1
                if temp_remaining_digits[digit] == 0:
                    del temp_remaining_digits[digit]
                
                new_num = current_num + digit
                
                if int(new_num) <= int(b[:len(new_num)]):
                    if len(new_num) == len(b[:len(new_num)]):
                         if int(new_num) <= int(b[:len(new_num)]):
                            possible_num = find_max_permutation(index + 1, new_num, temp_remaining_digits)
                            if possible_num != "" and (best_num == "" or int(possible_num) > int(best_num)):
                                best_num = possible_num
                    else:
                        possible_num = find_max_permutation(index + 1, new_num, temp_remaining_digits)
                        if possible_num != "" and (best_num == "" or int(possible_num) > int(best_num)):
                            best_num = possible_num
                    
        return best_num

    
    a_counts = Counter(list(a))
    result = find_max_permutation(0, "", a_counts)
    print(result)
    
solve()