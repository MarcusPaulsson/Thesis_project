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

    a_count = Counter(a)
    
    def find_max_permutation(index, current_num, remaining_count):
        if index == len(a):
            return current_num
        
        for digit in sorted(remaining_count.keys(), reverse=True):
            new_count = remaining_count.copy()
            new_count[digit] -= 1
            if new_count[digit] == 0:
                del new_count[digit]
            
            new_num = current_num + digit
            
            if new_num <= b:
                result = find_max_permutation(index + 1, new_num, new_count)
                if result is not None:
                    return result
        
        return None

    result = find_max_permutation(0, "", a_count)
    print(result)

solve()