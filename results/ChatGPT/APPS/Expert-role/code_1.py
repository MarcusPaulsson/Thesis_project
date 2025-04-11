def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_max_digit_sum(x):
    max_sum = sum_of_digits(x)
    best_number = x
    
    # Check numbers by reducing the last digits to 9
    str_x = str(x)
    for i in range(len(str_x)):
        if str_x[i] == '0':
            continue
        
        # Create a new number by reducing the current digit and setting the rest to 9
        new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (len(str_x) - i - 1)
        new_number = int(new_number)
        
        if new_number > 0 and new_number <= x:
            current_sum = sum_of_digits(new_number)
            if current_sum > max_sum or (current_sum == max_sum and new_number > best_number):
                max_sum = current_sum
                best_number = new_number

    return best_number

x = int(input().strip())
print(find_max_digit_sum(x))