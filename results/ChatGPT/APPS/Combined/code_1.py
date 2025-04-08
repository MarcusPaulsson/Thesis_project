def max_digit_sum_integer(x):
    str_x = str(x)
    length = len(str_x)
    max_sum = sum(int(d) for d in str_x)
    result = x

    for i in range(length):
        if str_x[i] != '0':
            # Create a candidate by decreasing the current digit and setting all following digits to 9
            candidate = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (length - i - 1)
            candidate_int = int(candidate)
            if candidate_int > 0:
                candidate_digit_sum = sum(int(d) for d in candidate)
                if (candidate_digit_sum > max_sum) or (candidate_digit_sum == max_sum and candidate_int > result):
                    max_sum = candidate_digit_sum
                    result = candidate_int

    return result

x = int(input().strip())
print(max_digit_sum_integer(x))