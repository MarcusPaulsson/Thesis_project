from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    b_digits = list(b)
    
    if len(a) < len(b):
        print("".join(a_digits))
        return
    
    def find_max_permutation(index, remaining_digits, current_number):
        if index == len(a):
            return current_number
        
        best_number = ""
        
        for digit in sorted(remaining_digits.keys(), reverse=True):
            if remaining_digits[digit] > 0:
                if digit < b_digits[index]:
                    temp_digits = remaining_digits.copy()
                    temp_digits[digit] -= 1
                    
                    remaining_str = ""
                    for d in sorted(temp_digits.keys(), reverse=True):
                        remaining_str += d * temp_digits[d]
                    
                    new_number = current_number + digit + remaining_str
                    
                    if best_number == "" or new_number > best_number:
                        best_number = new_number
                elif digit == b_digits[index]:
                    temp_digits = remaining_digits.copy()
                    temp_digits[digit] -= 1
                    
                    next_remaining_digits = {k: v for k, v in temp_digits.items() if v > 0}
                    
                    next_number = find_max_permutation(index + 1, temp_digits, current_number + digit)
                    
                    if next_number != "" and (best_number == "" or next_number > best_number):
                        best_number = next_number
        
        return best_number
    
    a_counts = Counter(a)
    result = find_max_permutation(0, a_counts, "")
    print(result)

solve()