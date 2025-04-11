def solve():
    k = int(input())
    
    digits = 0
    count = 0
    power_of_10 = 1
    length = 1
    
    while True:
        num_digits = 9 * power_of_10 * length
        if digits + num_digits >= k:
            break
        digits += num_digits
        power_of_10 *= 10
        length += 1
    
    diff = k - digits - 1
    number_index = diff // length
    digit_index = diff % length
    
    number = power_of_10 + number_index
    
    print(str(number)[digit_index])

solve()