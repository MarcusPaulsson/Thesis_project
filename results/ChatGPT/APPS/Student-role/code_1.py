def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    max_sum = sum(int(d) for d in str_x)
    best_number = x

    for i in range(n):
        if str_x[i] == '0':
            continue

        # Create a new number by reducing the current digit
        new_number = list(str_x)
        new_number[i] = str(int(new_number[i]) - 1)
        for j in range(i + 1, n):
            new_number[j] = '9'  # Set all subsequent digits to 9

        candidate = int(''.join(new_number))
        if candidate <= x:
            current_sum = sum(int(d) for d in str(candidate))
            if current_sum > max_sum or (current_sum == max_sum and candidate > best_number):
                max_sum = current_sum
                best_number = candidate

    return best_number

x = int(input())
print(max_digit_sum(x))