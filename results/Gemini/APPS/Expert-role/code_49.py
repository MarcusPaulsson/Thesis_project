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
        count += 9 * power_of_10
        power_of_10 *= 10
        length += 1
    
    remaining = k - digits
    num_index = (remaining - 1) // length
    digit_index = (remaining - 1) % length
    
    number = power_of_10 + num_index
    
    print(str(number)[digit_index])

solve()