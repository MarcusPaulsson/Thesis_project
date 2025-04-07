def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def max_sum_digit_number(x):
    s = str(x)
    n = len(s)
    
    max_number = x
    max_digit_sum = sum_of_digits(x)

    for i in range(n):
        if s[i] != '0':
            new_number = list(s)
            new_number[i] = str(int(s[i]) - 1)
            new_number[i + 1:] = '9' * (n - i - 1)
            new_number = int(''.join(new_number))
            
            if new_number > 0 and new_number <= x:
                current_digit_sum = sum_of_digits(new_number)
                if (current_digit_sum > max_digit_sum) or (current_digit_sum == max_digit_sum and new_number > max_number):
                    max_number = new_number
                    max_digit_sum = current_digit_sum

    return max_number

x = int(input().strip())
print(max_sum_digit_number(x))