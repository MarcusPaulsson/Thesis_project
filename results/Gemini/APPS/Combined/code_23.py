from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    
    if len(a) < len(b):
        print("".join(a_digits))
        return
    
    a_counts = Counter(a)
    
    def find_max_permutation(index, current_num, remaining_counts):
        if index == len(a):
            return current_num
        
        for digit in sorted(remaining_counts.keys(), reverse=True):
            
            if current_num == "" and digit == '0':
                continue
            
            temp_counts = remaining_counts.copy()
            temp_counts[digit] -= 1
            if temp_counts[digit] == 0:
                del temp_counts[digit]
            
            new_num = current_num + digit
            
            if len(new_num) < len(b) or new_num <= b:
                result = find_max_permutation(index + 1, new_num, temp_counts)
                if result is not None:
                    return result
        
        return None

    result = find_max_permutation(0, "", a_counts)
    print(result)

solve()