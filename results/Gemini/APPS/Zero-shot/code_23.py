from collections import Counter

def solve():
    a = input()
    b = input()

    a_digits = sorted(list(a), reverse=True)
    b_digits = list(b)

    if len(a) < len(b):
        print("".join(sorted(list(a), reverse=True)))
        return

    if len(a) > len(b):
        print("".join(sorted(list(a), reverse=True)))
        return
    
    a_count = Counter(a)
    
    def find_max(index, current_num, remaining_count):
        if index == len(a):
            return current_num
        
        best_num = ""
        
        for digit in sorted(remaining_count.keys(), reverse=True):
            if int(digit) > int(b_digits[index]):
                continue
            
            if remaining_count[digit] == 0:
                continue
                
            new_count = remaining_count.copy()
            new_count[digit] -= 1
            
            if new_count[digit] == 0:
                del new_count[digit]
            
            new_num = current_num + digit
            
            if int(digit) < int(b_digits[index]):
                remaining_digits = []
                for d, count in new_count.items():
                    remaining_digits.extend([d] * count)
                
                remaining_digits.sort(reverse=True)
                
                if remaining_digits:
                    temp_num = new_num + "".join(remaining_digits)
                    if not best_num or int(temp_num) > int(best_num):
                        best_num = temp_num
                else:
                    if not best_num or int(new_num) > int(best_num):
                        best_num = new_num
            else:
                temp_num = find_max(index+1, new_num, new_count)
                if temp_num and (not best_num or int(temp_num) > int(best_num)):
                    best_num = temp_num
                    
        return best_num

    result = find_max(0, "", a_count)
    print(result)

solve()