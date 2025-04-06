def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def max_digit_sum(x):
    max_sum = sum_of_digits(x)
    best_number = x
    
    # Check numbers by reducing the last digits to 9
    str_x = str(x)
    for i in range(len(str_x)):
        if str_x[i] == '0':
            continue
        
        # Create a candidate by reducing the current digit and setting all following digits to 9
        candidate = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (len(str_x) - i - 1)
        candidate = int(candidate)
        
        if candidate > 0 and candidate <= x:
            current_sum = sum_of_digits(candidate)
            if current_sum > max_sum or (current_sum == max_sum and candidate > best_number):
                max_sum = current_sum
                best_number = candidate
    
    return best_number

x = int(input().strip())
print(max_digit_sum(x))