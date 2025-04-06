def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    
    # Function to calculate the sum of digits of a number
    def digit_sum(num):
        return sum(int(d) for d in str(num))
    
    max_sum = digit_sum(x)
    max_number = x
    
    for i in range(n):
        if str_x[i] != '0':
            # Create a new number by reducing the current digit by 1 and making all following digits 9
            new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
            new_number = int(new_number)
            if new_number > 0:  # Ensure the number is positive
                current_sum = digit_sum(new_number)
                if (current_sum > max_sum) or (current_sum == max_sum and new_number > max_number):
                    max_sum = current_sum
                    max_number = new_number
    
    return max_number

# Input
x = int(input())
# Output
print(max_digit_sum(x))