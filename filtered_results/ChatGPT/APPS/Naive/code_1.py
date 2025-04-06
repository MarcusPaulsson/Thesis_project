def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    
    max_sum = 0
    result = x

    for i in range(n):
        if str_x[i] == '0':
            continue

        # Create a new number by reducing the current digit and setting all following digits to '9'
        new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        new_number = int(new_number)

        if new_number > 0 and new_number <= x:
            digit_sum = sum(int(d) for d in str(new_number))
            if (digit_sum > max_sum) or (digit_sum == max_sum and new_number > result):
                max_sum = digit_sum
                result = new_number

    # Check the original number itself
    original_sum = sum(int(d) for d in str_x)
    if original_sum > max_sum or (original_sum == max_sum and x > result):
        result = x

    return result

x = int(input())
print(max_digit_sum(x))