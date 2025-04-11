def max_digit_sum(x):
    str_x = str(x)
    n = len(str_x)
    
    best_number = x
    max_digit_sum = sum(int(digit) for digit in str_x)
    
    for i in range(n):
        if str_x[i] == '0':
            continue
        
        # Create a candidate by reducing the current digit and setting all following digits to '9'
        candidate = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (n - i - 1)
        candidate_int = int(candidate)
        
        if candidate_int <= x:
            candidate_digit_sum = sum(int(digit) for digit in candidate)
            if (candidate_digit_sum > max_digit_sum) or (candidate_digit_sum == max_digit_sum and candidate_int > best_number):
                best_number = candidate_int
                max_digit_sum = candidate_digit_sum
    
    return best_number

if __name__ == "__main__":
    x = int(input().strip())
    print(max_digit_sum(x))