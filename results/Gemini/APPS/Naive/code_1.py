def solve():
    x = int(input())
    
    def sum_digits(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

    best_num = x
    max_sum = sum_digits(x)

    s = str(x)
    n = len(s)

    for i in range(n):
        if s[i] == '0':
            continue
        
        prefix = int(s[:i]) if i > 0 else 0
        
        current_num = (prefix * (10**(n-i-1))) + ((int(s[i]) -1) * (10**(n-i-1))) + (10**(n-i-1) -1)
        
        if current_num <= 0:
            continue
        
        if current_num <= x:
            current_sum = sum_digits(current_num)

            if current_sum > max_sum:
                max_sum = current_sum
                best_num = current_num
            elif current_sum == max_sum and current_num > best_num:
                best_num = current_num

    print(best_num)

solve()