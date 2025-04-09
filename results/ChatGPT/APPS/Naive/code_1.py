def max_digit_sum_number(x):
    str_x = str(x)
    n = len(str_x)
    
    # Initialize the best number and maximum digit sum
    best_number = x
    max_digit_sum = sum(int(d) for d in str_x)

    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a new candidate by reducing the current digit and filling the rest with '9'
        candidate = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        candidate_int = int(candidate)

        if candidate_int > 0 and candidate_int <= x:
            candidate_digit_sum = sum(int(d) for d in candidate)
            if (candidate_digit_sum > max_digit_sum or 
                (candidate_digit_sum == max_digit_sum and candidate_int > best_number)):
                best_number = candidate_int
                max_digit_sum = candidate_digit_sum

    return best_number

x = int(input())
print(max_digit_sum_number(x))