def max_digit_sum_number(x):
    # Convert x to string to easily manipulate digits
    str_x = str(x)
    n = len(str_x)
    
    # Initialize the maximum sum and the number that gives this sum
    max_sum = 0
    result_number = x
    
    # Iterate over each digit
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new number by reducing the current digit by 1 and setting all following digits to 9
        new_number = list(str_x)
        new_number[i] = str(int(new_number[i]) - 1)
        new_number[i+1:] = ['9'] * (n - i - 1)
        
        # Convert back to integer
        candidate = int(''.join(new_number))
        
        # Check if candidate is valid
        if candidate > 0 and candidate <= x:
            # Calculate sum of digits of candidate
            digit_sum = sum(int(d) for d in str(candidate))
            
            # Update result if we found a better candidate
            if (digit_sum > max_sum) or (digit_sum == max_sum and candidate > result_number):
                max_sum = digit_sum
                result_number = candidate
    
    return result_number

# Input reading
x = int(input().strip())
print(max_digit_sum_number(x))