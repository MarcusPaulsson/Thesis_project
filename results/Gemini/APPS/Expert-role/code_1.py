def solve():
    x = int(input())
    
    best_num = x
    max_sum = sum_digits(x)
    
    s = str(x)
    n = len(s)
    
    for i in range(n):
        if s[i] == '0':
            continue
        
        num_str = s[:i] + str(int(s[i]) - 1) + '9' * (n - i - 1)
        num = int(num_str)
        
        if num <= 0:
            continue
        
        current_sum = sum_digits(num)
        
        if current_sum > max_sum:
            max_sum = current_sum
            best_num = num
        elif current_sum == max_sum and num > best_num:
            best_num = num
            
    print(best_num)

def sum_digits(n):
    s = str(n)
    sum_val = 0
    for digit in s:
        sum_val += int(digit)
    return sum_val

solve()