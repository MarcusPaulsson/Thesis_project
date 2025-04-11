from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    
    if len(a) < len(b):
        print("".join(a_digits))
        return
    
    a_count = Counter(a)
    
    def find_max(index, current_num, remaining_count, is_smaller):
        if index == len(a):
            return current_num
        
        best_num = ""
        
        possible_digits = sorted(remaining_count.keys(), reverse=True)
        
        for digit in possible_digits:
            if not is_smaller and digit > b[index]:
                continue
            
            new_count = remaining_count.copy()
            new_count[digit] -= 1
            if new_count[digit] == 0:
                del new_count[digit]
            
            new_is_smaller = is_smaller or digit < b[index]
            
            result = find_max(index + 1, current_num + digit, new_count, new_is_smaller)
            
            if len(result) == len(a) and (best_num == "" or result > best_num):
                best_num = result
        
        return best_num
    
    result = find_max(0, "", a_count, False)
    print(result)

solve()