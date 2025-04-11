def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    
    # Start with the maximum possible number which is x itself
    max_num = x
    max_sum = sum(int(d) for d in str_x)
    
    # Check numbers by reducing digits
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new number by reducing the current digit and setting all following digits to 9
        new_num = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        new_num = int(new_num)
        
        if new_num > 0 and new_num <= x:
            new_sum = sum(int(d) for d in str(new_num))
            if new_sum > max_sum or (new_sum == max_sum and new_num > max_num):
                max_num = new_num
                max_sum = new_sum
    
    return max_num

x = int(input())
print(max_digit_sum(x))