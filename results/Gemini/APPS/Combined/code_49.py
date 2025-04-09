def solve():
    k = int(input())
    
    digits_count = 0
    length = 1
    power_of_10 = 1
    
    while True:
        numbers_count = 9 * power_of_10
        total_digits = numbers_count * length
        
        if digits_count + total_digits >= k:
            break
        
        digits_count += total_digits
        length += 1
        power_of_10 *= 10
    
    remaining = k - digits_count
    number_index = (remaining - 1) // length
    digit_index = (remaining - 1) % length
    
    number = power_of_10 + number_index
    
    print(str(number)[digit_index])

solve()