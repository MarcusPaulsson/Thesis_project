def digit_sum(n):
    return sum(int(d) for d in str(n))

def max_digit_sum(x):
    max_sum = digit_sum(x)
    best_number = x
    
    str_x = str(x)
    n = len(str_x)
    
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a candidate by reducing the current digit and setting following digits to 9
        candidate = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        candidate = int(candidate)
        
        if candidate > 0:
            current_sum = digit_sum(candidate)
            if current_sum > max_sum or (current_sum == max_sum and candidate > best_number):
                max_sum = current_sum
                best_number = candidate
    
    return best_number

x = int(input().strip())
print(max_digit_sum(x))