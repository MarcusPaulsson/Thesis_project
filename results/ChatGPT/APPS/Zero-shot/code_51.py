def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    
    # Start with the original number
    max_sum = sum(int(d) for d in str_x)
    best_number = x
    
    # Try modifying each digit from left to right
    for i in range(n):
        # Create a new number by reducing the current digit by 1 and setting all following digits to 9
        if str_x[i] == '0':
            continue
        
        new_number = list(str_x)
        new_number[i] = str(int(new_number[i]) - 1)  # Decrease current digit by 1
        for j in range(i + 1, n):
            new_number[j] = '9'  # Set all following digits to 9
            
        candidate = int(''.join(new_number))
        
        # Ignore candidates that are greater than x
        if candidate > x:
            continue
        
        # Calculate the sum of digits of the candidate
        candidate_sum = sum(int(d) for d in str(candidate))
        
        # Update if we find a better candidate
        if candidate_sum > max_sum or (candidate_sum == max_sum and candidate > best_number):
            max_sum = candidate_sum
            best_number = candidate
    
    return best_number

x = int(input().strip())
print(max_digit_sum(x))