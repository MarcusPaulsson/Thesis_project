def max_digit_sum(x):
    x = str(x)
    n = len(x)
    max_sum = sum(int(digit) for digit in x)
    max_number = int(x)
    
    for i in range(n):
        for j in range(9, -1, -1):
            new_number = x[:i] + str(j) + '9' * (n - i - 1)
            if int(new_number) <= int(x) and sum(int(digit) for digit in new_number) > max_sum:
                max_sum = sum(int(digit) for digit in new_number)
                max_number = int(new_number)
            elif sum(int(digit) for digit in new_number) == max_sum and int(new_number) > max_number:
                max_number = int(new_number)
    
    return max_number

x = int(input())
print(max_digit_sum(x))