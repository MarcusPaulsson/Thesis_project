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

    def find_max_permutation(index, current_num, remaining_digits):
        if index == len(a):
            return current_num

        best_num = ""
        for digit in sorted(list(set(remaining_digits)), reverse=True):
            temp_digits = remaining_digits[:]
            temp_digits.remove(digit)
            
            if current_num + digit <= b[:index+1]:
                next_num = find_max_permutation(index + 1, current_num + digit, temp_digits)
                if next_num != "" and (best_num == "" or int(next_num) > int(best_num)):
                    best_num = next_num
                    
        return best_num
    
    from collections import Counter
    a_digits_list = list(a)
    
    counts = Counter(a_digits_list)

    def find_max_permutation_optimized(index, current_num, remaining_counts):
        if index == len(a):
            return current_num

        best_num = ""
        for digit in sorted(list(remaining_counts.keys()), reverse=True):
            if remaining_counts[digit] > 0:
                temp_counts = remaining_counts.copy()
                temp_counts[digit] -= 1
                if temp_counts[digit] == 0:
                    del temp_counts[digit]
                
                if current_num + digit <= b[:index+1]:
                    next_num = find_max_permutation_optimized(index + 1, current_num + digit, temp_counts)
                    if next_num != "" and (best_num == "" or int(next_num) > int(best_num)):
                        best_num = next_num
                    
        return best_num

    counts_dict = Counter(a)
    result = find_max_permutation_optimized(0, "", counts_dict)

    if result == "":
        print("".join(sorted(list(a), reverse=True)))
    else:
        print(result)
solve()