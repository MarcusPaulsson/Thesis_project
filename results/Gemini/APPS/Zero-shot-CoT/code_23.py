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
    
    
    
    def find_max_permutation(digits, target, index, current):
        if index == len(target):
            return current if current <= target else ""
        
        best_result = ""
        
        for i in range(len(digits)):
            new_digits = digits[:i] + digits[i+1:]
            new_current = current + digits[i]
            
            if new_current[:index] == target[:index] and digits[i] <= target[index]:
                result = find_max_permutation(new_digits, target, index + 1, new_current)
                if result != "":
                    if best_result == "" or result > best_result:
                        best_result = result
        
        return best_result

    
    digits = sorted(list(a), reverse=True)
    target = b
    result = find_max_permutation(digits, target, 0, "")
    
    if result == "":
        print("".join(sorted(list(a), reverse=True)))
    else:
        print(result)
        
solve()