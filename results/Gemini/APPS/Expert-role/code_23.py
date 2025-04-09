from collections import Counter

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
    
    a_count = Counter(a)
    
    def find_max(index, current_num, remaining_count):
        if index == len(a):
            return current_num
        
        for digit in sorted(remaining_count.keys(), reverse=True):
            new_count = remaining_count.copy()
            new_count[digit] -= 1
            if new_count[digit] == 0:
                del new_count[digit]
            
            new_num = current_num + digit
            
            if new_num <= b:
                if len(new_num) == index + 1:

                    if len(new_count) == 0:
                         return new_num
                    
                    temp_digits = []
                    for d in new_count:
                        temp_digits.extend([d] * new_count[d])

                    temp_digits.sort(reverse=True)

                    
                    remaining_str = "".join(temp_digits)
                    
                    if len(new_num) + len(remaining_str) == len(a):
                        return new_num + remaining_str
                    
        return ""

    def find_ans(index, current_num, remaining_count, smaller):
        if index == len(a):
            return current_num
        
        if smaller:
            ans = ""
            for digit in sorted(remaining_count.keys(), reverse=True):
                new_count = remaining_count.copy()
                new_count[digit] -= 1
                if new_count[digit] == 0:
                    del new_count[digit]
                
                new_num = current_num + digit
                
                temp_digits = []
                for d in new_count:
                    temp_digits.extend([d] * new_count[d])

                temp_digits.sort(reverse=True)
                remaining_str = "".join(temp_digits)
                
                if len(new_num) + len(remaining_str) == len(a):
                    return new_num + remaining_str
            return ""
        
        digit_b = b[index]
        
        ans = ""
        
        for digit in sorted(remaining_count.keys(), reverse=True):
            if digit > digit_b:
                continue
            
            new_count = remaining_count.copy()
            new_count[digit] -= 1
            if new_count[digit] == 0:
                del new_count[digit]
            
            new_num = current_num + digit
            
            if digit < digit_b:
                temp_digits = []
                for d in new_count:
                    temp_digits.extend([d] * new_count[d])

                temp_digits.sort(reverse=True)
                remaining_str = "".join(temp_digits)

                if len(new_num) + len(remaining_str) == len(a):
                    return new_num + remaining_str
            else:
                res = find_ans(index + 1, new_num, new_count, False)
                if res:
                    return res
        
        return ""
    
    
    a_count = Counter(a)
    ans = find_ans(0, "", a_count, False)
    print(ans)

solve()