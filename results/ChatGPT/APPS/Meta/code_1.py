def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    
    # Start with the maximum number being x itself
    max_num = x
    max_sum = sum(int(d) for d in str_x)
    
    # Check numbers by reducing digits
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new number by reducing the current digit and setting the rest to 9
        new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        new_number = int(new_number)
        
        if new_number > 0 and new_number <= x:
            current_sum = sum(int(d) for d in str(new_number))
            if current_sum > max_sum or (current_sum == max_sum and new_number > max_num):
                max_num = new_number
                max_sum = current_sum
    
    return max_num

x = int(input())
print(max_digit_sum(x))