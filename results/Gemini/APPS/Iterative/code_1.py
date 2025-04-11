def solve():
    x = int(input())
    s = str(x)
    n = len(s)
    
    best_num = x
    best_sum = sum(int(digit) for digit in s)
    
    for i in range(n):
        if s[i] == '0':
            continue
        
        num_str = s[:i] + str(int(s[i]) - 1) + '9' * (n - i - 1)
        num = int(num_str)
        
        if num > 0 and num <= x:
            current_sum = sum(int(digit) for digit in num_str)
            if current_sum > best_sum:
                best_sum = current_sum
                best_num = num
            elif current_sum == best_sum and num > best_num:
                best_num = num
                
    print(best_num)

solve()