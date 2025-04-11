def find_kth_digit(k):
    digit_length = 1
    count = 9
    start = 1

    while k > digit_length * count:
        k -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    start += (k - 1) // digit_length
    number = str(start)
    return int(number[(k - 1) % digit_length])

k = int(input().strip())
print(find_kth_digit(k))