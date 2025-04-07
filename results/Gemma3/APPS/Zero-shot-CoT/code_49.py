def solve():
    k = int(input())
    
    digit_count = 0
    num_digits = 1
    num = 1
    
    while digit_count + num_digits * (num + 1) - num_digits < k:
        digit_count += num_digits * (num + 1) - num_digits
        num_digits += 1
        num *= 10
    
    remaining = k - digit_count
    
    index_within_num = (remaining - 1) // num_digits
    
    number = num + index_within_num
    
    digit_index = (remaining - 1) % num_digits
    
    digit = int(str(number)[digit_index])
    
    print(digit)

solve()