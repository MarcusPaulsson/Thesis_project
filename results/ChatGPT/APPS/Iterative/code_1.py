def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    
    # Start with the original number
    max_sum = sum(int(d) for d in str_x)
    best_number = x
    
    # Try to create numbers by reducing digits
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new number by reducing the current digit by 1 and setting all following digits to 9
        new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        new_number = int(new_number)
        
        if new_number <= x:
            current_sum = sum(int(d) for d in str(new_number))
            if current_sum > max_sum or (current_sum == max_sum and new_number > best_number):
                max_sum = current_sum
                best_number = new_number
    
    return best_number

x = int(input().strip())
print(max_digit_sum(x))