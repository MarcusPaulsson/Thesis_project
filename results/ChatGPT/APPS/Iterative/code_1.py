def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def max_sum_digits(x):
    str_x = str(x)
    n = len(str_x)

    # Start with the original number
    max_number = x
    max_digit_sum = sum_of_digits(x)

    # Generate candidates by reducing digits
    for i in range(n):
        if str_x[i] == '0':
            continue
        # Create a new candidate by reducing the current digit
        candidate = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        candidate_number = int(candidate)
        if candidate_number > 0 and candidate_number <= x:
            candidate_digit_sum = sum_of_digits(candidate_number)
            if (candidate_digit_sum > max_digit_sum or 
               (candidate_digit_sum == max_digit_sum and candidate_number > max_number)):
                max_number = candidate_number
                max_digit_sum = candidate_digit_sum

    return max_number

x = int(input().strip())
print(max_sum_digits(x))