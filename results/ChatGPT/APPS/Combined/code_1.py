def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    max_sum_number = x

    for i in range(n):
        if str_x[i] != '0':
            candidate = list(str_x)
            candidate[i] = str(int(candidate[i]) - 1)
            candidate[i+1:] = ['9'] * (n - i - 1)
            candidate_number = int(''.join(candidate))
            
            if candidate_number <= x:
                max_sum_number = max(max_sum_number, candidate_number)

    return max_sum_number

# Read input
x = int(input().strip())
# Output the result
print(max_digit_sum(x))