def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def max_sum_of_digits(x):
    str_x = str(x)
    n = len(str_x)
    
    # Start with the maximum number equal to x
    max_number = x
    max_digit_sum = sum_of_digits(x)

    # Try to create a number by reducing one digit and filling the rest with 9s
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new number by decrementing the current digit
        # and setting all subsequent digits to 9
        new_number = list(str_x)
        new_number[i] = str(int(new_number[i]) - 1)  # Decrease the digit
        for j in range(i + 1, n):
            new_number[j] = '9'  # Set all following digits to 9
        
        new_number = int(''.join(new_number))
        
        if new_number > 0 and new_number <= x:
            current_digit_sum = sum_of_digits(new_number)
            if current_digit_sum > max_digit_sum or (current_digit_sum == max_digit_sum and new_number > max_number):
                max_number = new_number
                max_digit_sum = current_digit_sum

    return max_number

x = int(input())
print(max_sum_of_digits(x))