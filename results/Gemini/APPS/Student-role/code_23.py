from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    
    def find_max_permutation(digits, target, index, current_num):
        if index == len(target):
            return current_num if current_num <= target else ""

        available_digits = Counter(digits)
        
        for digit in sorted(list(set(digits)), reverse=True):
            if available_digits[digit] > 0:
                remaining_digits = list(digits)
                remaining_digits.remove(digit)
                
                new_num = current_num + digit
                
                if new_num < target[:index+1]:
                    remaining_digits.sort(reverse=True)
                    return new_num + "".join(remaining_digits)
                elif new_num == target[:index+1]:
                    res = find_max_permutation(remaining_digits, target, index + 1, new_num)
                    if res:
                        return res
                
        return ""
    
    if len(a) < len(b):
        a_digits.sort(reverse=True)
        print("".join(a_digits))
    elif len(a) == len(b):
        res = find_max_permutation(list(a), b, 0, "")
        print(res)
    
solve()