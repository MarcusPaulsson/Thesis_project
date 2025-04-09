from collections import Counter

def solve():
    a = input()
    b = input()

    a_digits = sorted(list(a), reverse=True)
    
    if len(a) < len(b):
        print("".join(a_digits))
        return
    
    a_counts = Counter(a)
    
    def find_max(idx, current_num, remaining_counts):
        if idx == len(a):
            return current_num
        
        best_num = ""
        
        for digit in sorted(remaining_counts.keys(), reverse=True):
            temp_counts = remaining_counts.copy()
            
            if temp_counts[digit] > 0:
                temp_counts[digit] -= 1
                if temp_counts[digit] == 0:
                    del temp_counts[digit]
                    
                new_num = current_num + digit
                
                if len(new_num) <= len(b):
                    if len(new_num) < len(b) or new_num <= b:
                        result = find_max(idx + 1, new_num, temp_counts)
                        if len(result) > len(best_num):
                            best_num = result
                        elif len(result) == len(best_num) and result > best_num:
                            best_num = result
        
        return best_num

    result = find_max(0, "", a_counts)
    print(result)

solve()