def solve():
    k = int(input())

    digits = 0
    length = 1
    power_of_10 = 1

    while True:
        num_count = 9 * power_of_10
        num_digits = num_count * length

        if digits + num_digits >= k:
            break

        digits += num_digits
        power_of_10 *= 10
        length += 1

    remaining = k - digits
    num_index = (remaining - 1) // length
    digit_index = (remaining - 1) % length

    number = power_of_10 + num_index

    print(str(number)[digit_index])

solve()