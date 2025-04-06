def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def max_digit_sum(x):
    # Start by considering x itself
    max_sum = sum_of_digits(x)
    result = x

    # Check numbers by reducing the last digits to 9
    str_x = str(x)
    length = len(str_x)

    # Generate candidates by changing digits to 9
    for i in range(length):
        if str_x[i] == '0':
            continue
        # Create a new number by reducing the current digit and making all following digits 9
        candidate = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (length - i - 1)
        candidate = int(candidate)
        if candidate <= x:
            candidate_sum = sum_of_digits(candidate)
            if candidate_sum > max_sum or (candidate_sum == max_sum and candidate > result):
                max_sum = candidate_sum
                result = candidate

    return result

x = int(input())
print(max_digit_sum(x))