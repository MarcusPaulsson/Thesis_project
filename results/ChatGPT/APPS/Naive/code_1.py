def max_digit_sum_number(x):
    str_x = str(x)
    n = len(str_x)
    
    # Start with the original number
    max_number = x
    max_digit_sum = sum(int(d) for d in str_x)
    
    # Check numbers by reducing digits
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new number by reducing the current digit and setting all following digits to 9
        new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        new_number = int(new_number)
        
        if new_number > 0:
            new_digit_sum = sum(int(d) for d in str(new_number))
            if new_digit_sum > max_digit_sum or (new_digit_sum == max_digit_sum and new_number > max_number):
                max_number = new_number
                max_digit_sum = new_digit_sum
    
    return max_number

# Input
x = int(input().strip())
# Output
print(max_digit_sum_number(x))