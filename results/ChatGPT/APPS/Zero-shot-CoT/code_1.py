def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)

    # Initialize the maximum sum of digits and the result number
    max_sum = 0
    result = x

    # Check all numbers by changing each digit from the left to '0'
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new number by changing the current digit to one less and setting all following digits to '9'
        new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        new_number = int(new_number)

        # Calculate the sum of digits
        digit_sum = sum(int(d) for d in str(new_number))
        
        # Update the result if the new digit sum is greater or equal to the max_sum
        if digit_sum > max_sum or (digit_sum == max_sum and new_number > result):
            max_sum = digit_sum
            result = new_number

    return result

# Input
x = int(input())
# Output the result
print(max_digit_sum(x))