def find_kth_digit(k):
    length = 1  # Length of numbers we are currently considering
    count = 9   # Count of numbers with the current length
    start = 1   # Starting number with the current length

    # Determine the range where the k-th digit falls
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10

    # Find the actual number that contains the k-th digit
    start += (k - 1) // length
    number_str = str(start)
    
    # Find the exact digit
    digit_index = (k - 1) % length
    return number_str[digit_index]

k = int(input().strip())
print(find_kth_digit(k))