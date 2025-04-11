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
        power_of_10 *= 10
        length += 1

    remaining_digits = k - digits_count
    number_index = (remaining_digits - 1) // length
    digit_index = (remaining_digits - 1) % length

    number = power_of_10 + number_index
    number_str = str(number)

    print(number_str[digit_index])

solve()