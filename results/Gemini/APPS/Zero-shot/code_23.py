from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    a_len = len(a)
    b_len = len(b)

    if a_len > b_len:
        print("".join(a_digits))
        return
    
    a_counts = Counter(a)
    
    def find_max(index, current_num, remaining_counts, smaller):
        if index == a_len:
            return current_num
        
        best_num = ""
        
        possible_digits = sorted(remaining_counts.keys(), reverse=True)
        
        for digit in possible_digits:
            if smaller or digit <= b[index]:
                new_remaining_counts = remaining_counts.copy()
                new_remaining_counts[digit] -= 1
                if new_remaining_counts[digit] == 0:
                    del new_remaining_counts[digit]
                    
                new_smaller = smaller or digit < b[index]
                
                temp_num = find_max(index + 1, current_num + digit, new_remaining_counts, new_smaller)
                
                if len(temp_num) == a_len and (best_num == "" or temp_num > best_num):
                    best_num = temp_num
        
        return best_num
    
    result = find_max(0, "", a_counts, False)
    print(result)

solve()