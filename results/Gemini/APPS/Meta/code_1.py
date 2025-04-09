def solve():
    x = int(input())
    
    best_num = x
    best_sum = sum_digits(x)
    
    s = str(x)
    n = len(s)
    
    for i in range(n):
        if s[i] == '0':
            continue
        
        num_str = s[:i] + str(int(s[i]) - 1) + '9' * (n - i - 1)
        num = int(num_str)
        
        if num > 0:
            current_sum = sum_digits(num)
            if current_sum > best_sum:
                best_sum = current_sum
                best_num = num
            elif current_sum == best_sum and num > best_num:
                best_num = num
                
    print(best_num)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

solve()