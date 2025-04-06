def digit_sum(n):
    return sum(int(d) for d in str(n))

def max_digit_sum(x):
    max_sum = digit_sum(x)
    result = x
    
    # Check numbers with digits reduced to 9
    str_x = str(x)
    for i in range(len(str_x)):
        if str_x[i] == '0':
            continue
            
        # Create a new number by reducing the current digit and setting the rest to 9
        new_number = str_x[:i] + str(int(str_x[i]) - 1) + '9' * (len(str_x) - i - 1)
        new_number = int(new_number)
        
        if new_number <= x:
            current_sum = digit_sum(new_number)
            if current_sum > max_sum or (current_sum == max_sum and new_number > result):
                max_sum = current_sum
                result = new_number
    
    return result

x = int(input())
print(max_digit_sum(x))