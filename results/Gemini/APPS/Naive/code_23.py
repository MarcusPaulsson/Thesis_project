from collections import Counter

def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    b_digits = list(b)
    
    n_a = len(a)
    n_b = len(b)
    
    if n_a > n_b:
        print("".join(a_digits))
        return
    
    a_counts = Counter(a)
    
    def find_max_permutation(index, current_num, remaining_counts):
        if index == n_a:
            return current_num
        
        best_num = ""
        
        for digit in sorted(remaining_counts.keys(), reverse=True):
            if remaining_counts[digit] > 0:
                new_counts = remaining_counts.copy()
                new_counts[digit] -= 1
                if new_counts[digit] == 0:
                    del new_counts[digit]
                
                new_num = current_num + digit
                
                if int(new_num) <= int("".join(b_digits[:index+1])):
                    
                    if len(new_num) == len("".join(b_digits[:index+1])):
                        if int(new_num) <= int("".join(b_digits[:index+1])):
                            result = find_max_permutation(index+1, new_num, new_counts)
                            if len(result) == n_a:
                                if best_num == "" or int(result) > int(best_num):
                                    best_num = result
                    else:
                        remaining_digits = []
                        for d, count in new_counts.items():
                            remaining_digits.extend([d] * count)
                        remaining_digits.sort(reverse=True)
                        
                        temp_result = new_num + "".join(remaining_digits)
                        
                        if best_num == "" or int(temp_result) > int(best_num):
                            best_num = temp_result

        return best_num

    result = find_max_permutation(0, "", a_counts)
    print(result)

solve()