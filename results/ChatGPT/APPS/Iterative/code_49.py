def find_kth_digit(k):
    digit_length = 1
    count = 9
    start = 1

    # Determine the range in which the k-th digit falls
    while k > digit_length * count:
        k -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    # Find the actual number that contains the k-th digit
    number = start + (k - 1) // digit_length
    digit_index = (k - 1) % digit_length

    # Extract the specific digit from the number
    return str(number)[digit_index]

k = int(input())
print(find_kth_digit(k))