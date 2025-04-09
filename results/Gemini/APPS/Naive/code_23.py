from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_counts = Counter(a)
    
    def find_max_permutation(index, current_num, remaining_counts, b_str):
        if index == len(a):
            return current_num
        
        max_num = ""
        
        for digit in sorted(remaining_counts.keys(), reverse=True):
            if remaining_counts[digit] > 0:
                temp_counts = remaining_counts.copy()
                temp_counts[digit] -= 1
                
                new_num = current_num + digit
                
                if len(new_num) < len(b_str) or new_num <= b_str:
                    
                    valid = True
                    if len(new_num) == len(b_str):
                        for i in range(len(new_num)):
                            if new_num[i] > b_str[i]:
                                valid = False
                                break
                    
                    if valid:
                        
                        next_max = find_max_permutation(index + 1, new_num, temp_counts, b_str)
                        
                        if len(next_max) > len(max_num) or (len(next_max) == len(max_num) and next_max > max_num):
                            max_num = next_max
        
        return max_num

    result = find_max_permutation(0, "", a_counts, b)
    print(result)

solve()