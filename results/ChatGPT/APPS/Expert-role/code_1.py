def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    
    # Start with the original number
    max_number = x
    max_sum = sum(int(d) for d in str_x)
    
    # Try to create numbers by reducing digits
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new number by reducing the current digit and setting all following digits to 9
        new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        new_number = int(new_number)
        
        if new_number > 0 and new_number <= x:
            new_sum = sum(int(d) for d in str(new_number))
            if new_sum > max_sum or (new_sum == max_sum and new_number > max_number):
                max_number = new_number
                max_sum = new_sum
    
    return max_number

x = int(input())
print(max_digit_sum(x))