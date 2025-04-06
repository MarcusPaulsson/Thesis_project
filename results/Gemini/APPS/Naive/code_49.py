def solve():
    k = int(input())
    
    digits_count = 0
    power_of_10 = 1
    digits = 1
    
    while True:
        count_of_numbers = 9 * power_of_10
        total_digits = count_of_numbers * digits
        
        if digits_count + total_digits >= k:
            break
        
        digits_count += total_digits
        power_of_10 *= 10
        digits += 1

    remaining_digits = k - digits_count
    
    number_index = (remaining_digits - 1) // digits
    digit_index = (remaining_digits - 1) % digits
    
    number = power_of_10 + number_index
    
    print(str(number)[digit_index])

solve()