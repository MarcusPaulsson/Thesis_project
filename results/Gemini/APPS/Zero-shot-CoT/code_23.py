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
            new_counts = remaining_counts.copy()
            new_counts[digit] -= 1
            if new_counts[digit] == 0:
                del new_counts[digit]
            
            new_num = current_num + digit
            
            if int(new_num) > int(b[:index+1]) and len(new_num) == index + 1:
                continue
            
            if int(new_num) < int(b[:index+1]) and len(new_num) == index + 1:
                remaining_digits = []
                for d, count in new_counts.items():
                    remaining_digits.extend([d] * count)
                remaining_digits.sort(reverse=True)
                return new_num + "".join(remaining_digits)
            
            if int(new_num) == int(b[:index+1]) and len(new_num) == index + 1:
                result = find_max_permutation(index + 1, new_num, new_counts)
                if result:
                    return result
        
        return None

    result = find_max_permutation(0, "", a_counts)
    
    if result:
        print(result)
    else:
        print("".join(sorted(list(a), reverse=True)))

solve()