def solve():
    k = int(input())
    
    digits = 0
    count = 0
    power_of_10 = 1
    length = 1
    
    while True:
        num_numbers = 9 * power_of_10
        num_digits = num_numbers * length
        
        if count + num_digits >= k:
            break
        
        count += num_digits
        length += 1
        power_of_10 *= 10
    
    remaining = k - count
    number_index = (remaining - 1) // length
    digit_index = (remaining - 1) % length
    
    number = power_of_10 + number_index
    number_str = str(number)
    
    print(number_str[digit_index])

solve()