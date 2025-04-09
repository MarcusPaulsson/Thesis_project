from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_counts = Counter(a)
    n = len(a)
    m = len(b)

    if n < m:
        print("".join(sorted(a, reverse=True)))
        return

    def find_max(index, current_num, remaining_counts, less):
        if index == n:
            return current_num
        
        best_num = ""
        
        available_digits = sorted(remaining_counts.keys(), reverse=True)
        
        for digit in available_digits:
            if not less and digit > b[index]:
                continue
            
            new_counts = remaining_counts.copy()
            new_counts[digit] -= 1
            if new_counts[digit] == 0:
                del new_counts[digit]
            
            new_less = less or digit < b[index]
            
            result = find_max(index + 1, current_num + digit, new_counts, new_less)
            
            if len(result) == n and (best_num == "" or result > best_num):
                best_num = result
        
        return best_num
    
    result = find_max(0, "", a_counts, False)
    print(result)

solve()