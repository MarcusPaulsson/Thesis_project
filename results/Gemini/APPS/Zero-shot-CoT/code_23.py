def solve():
    a = input()
    b = input()
    
    a_digits = sorted(list(a), reverse=True)
    b_digits = list(b)
    
    if len(a) < len(b):
        print("".join(a_digits))
        return
    
    def find_max(index, current_digits, current_num, used):
        if index == len(a):
            return "".join(current_num)
        
        best_num = None
        
        available_digits = []
        for i in range(len(a_digits)):
            if not used[i]:
                available_digits.append(a_digits[i])
        
        available_digits = sorted(available_digits, reverse=True)
        
        for digit in available_digits:
            digit_index = -1
            for i in range(len(a_digits)):
                if a_digits[i] == digit and not used[i]:
                    digit_index = i
                    break
            
            if digit <= b_digits[index]:
                new_used = used[:]
                new_used[digit_index] = True
                new_num = current_num[:]
                new_num.append(digit)
                
                if digit < b_digits[index]:
                    remaining_digits = []
                    for i in range(len(a_digits)):
                        if not new_used[i]:
                            remaining_digits.append(a_digits[i])
                    
                    new_num.extend(sorted(remaining_digits, reverse=True))
                    
                    candidate = "".join(new_num)
                    if best_num is None or candidate > best_num:
                        best_num = candidate
                else:
                    candidate = find_max(index + 1, a_digits, new_num, new_used)
                    if candidate is not None and (best_num is None or candidate > best_num):
                        best_num = candidate
        
        return best_num

    used = [False] * len(a)
    result = find_max(0, a_digits, [], used)
    
    if result is None:
        print("".join(sorted(list(a), reverse=True)))
    else:
      print(result)

solve()