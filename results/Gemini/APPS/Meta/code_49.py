def solve():
    k = int(input())
    
    digits = 0
    count = 0
    power_of_10 = 1
    length = 1
    
    while True:
        num_numbers = 9 * power_of_10
        num_digits = num_numbers * length
        
        if digits + num_digits >= k:
            break
        
        digits += num_digits
        count += num_numbers
        power_of_10 *= 10
        length += 1
    
    remaining = k - digits
    number_index = (remaining - 1) // length
    digit_index = (remaining - 1) % length
    
    number = power_of_10 + number_index
    
    print(str(number)[digit_index])

solve()