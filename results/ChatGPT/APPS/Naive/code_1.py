def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    
    # Start with the maximum possible number which is x itself
    max_number = x
    max_sum = sum(int(d) for d in str_x)
    
    # Iterate through each digit to find the best candidate
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new number by reducing the current digit and setting all following digits to 9
        new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        new_number = int(new_number)
        
        if new_number > 0:
            current_sum = sum(int(d) for d in str(new_number))
            if current_sum > max_sum or (current_sum == max_sum and new_number > max_number):
                max_number = new_number
                max_sum = current_sum

    return max_number

x = int(input())
print(max_digit_sum(x))