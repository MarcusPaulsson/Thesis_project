def max_digit_sum(x):
    str_x = str(x)
    max_sum = sum(int(d) for d in str_x)
    best_number = x
    
    for i in range(len(str_x)):
        if str_x[i] == '0':
            continue
        
        candidate = list(str_x)
        candidate[i] = str(int(candidate[i]) - 1)
        candidate[i + 1:] = '9' * (len(candidate) - i - 1)
        
        candidate_number = int(''.join(candidate))
        
        if candidate_number <= x:
            candidate_sum = sum(int(d) for d in str(candidate_number))
            if (candidate_sum > max_sum) or (candidate_sum == max_sum and candidate_number > best_number):
                max_sum = candidate_sum
                best_number = candidate_number
    
    return best_number

if __name__ == "__main__":
    x = int(input().strip())
    print(max_digit_sum(x))