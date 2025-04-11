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
        
        best_num = None
        
        for digit in sorted(remaining_counts.keys(), reverse=True):
            if remaining_counts[digit] > 0:
                new_counts = remaining_counts.copy()
                new_counts[digit] -= 1
                if new_counts[digit] == 0:
                    del new_counts[digit]
                    
                new_num = current_num + digit
                
                if new_num <= b[:index+1]:
                    if new_num == b[:index+1]:
                        next_best = find_max_permutation(index + 1, new_num, new_counts)
                        if next_best is not None:
                            if best_num is None or next_best > best_num:
                                best_num = next_best
                    else:
                        remaining_digits = []
                        for d, count in new_counts.items():
                            remaining_digits.extend([d] * count)
                        remaining_digits.sort(reverse=True)
                        
                        full_num = new_num + "".join(remaining_digits)
                        if best_num is None or full_num > best_num:
                            best_num = full_num
        
        return best_num

    result = find_max_permutation(0, "", a_counts)
    print(result)

solve()