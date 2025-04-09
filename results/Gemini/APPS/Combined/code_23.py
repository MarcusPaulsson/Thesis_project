from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    n_a = len(a)
    n_b = len(b)
    
    if n_a > n_b:
        print("".join(a_digits))
        return
    
    def find_max_permutation(index, remaining_digits, current_num):
        if index == n_a:
            return current_num
        
        best_num = ""
        
        for digit in sorted(remaining_digits.keys(), reverse=True):
            if remaining_digits[digit] > 0:
                temp_remaining_digits = remaining_digits.copy()
                temp_remaining_digits[digit] -= 1
                if temp_remaining_digits[digit] == 0:
                    del temp_remaining_digits[digit]
                    
                new_num = current_num + digit
                
                if new_num <= b[:index+1]:
                    if len(new_num) < n_a:
                        if new_num < b[:index+1]:
                            sorted_rem = sorted(temp_remaining_digits.keys(), reverse=True)
                            rem_str = ""
                            for d in sorted_rem:
                                rem_str += d * temp_remaining_digits[d]
                            
                            candidate = new_num + rem_str
                            if len(candidate) == n_a:
                                if best_num == "" or candidate > best_num:
                                    best_num = candidate
                        else:
                            candidate = find_max_permutation(index + 1, temp_remaining_digits, new_num)
                            if candidate != "" and (best_num == "" or candidate > best_num):
                                best_num = candidate
                    else:
                        best_num = new_num
        
        return best_num

    a_counts = Counter(a)
    result = find_max_permutation(0, a_counts, "")
    
    print(result)

solve()