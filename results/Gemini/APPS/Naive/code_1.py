def solve():
    x = int(input())
    
    best_num = x
    max_digit_sum = sum_digits(x)
    
    s = str(x)
    n = len(s)
    
    for i in range(n):
        if s[i] == '0':
            continue
        
        num_str = s[:i] + str(int(s[i]) - 1) + '9' * (n - i - 1)
        num = int(num_str)
        
        if num > 0:
            digit_sum = sum_digits(num)
            
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
                best_num = num
            elif digit_sum == max_digit_sum and num > best_num:
                best_num = num
                
    print(best_num)

def sum_digits(n):
    s = str(n)
    digit_sum = 0
    for digit in s:
        digit_sum += int(digit)
    return digit_sum

solve()