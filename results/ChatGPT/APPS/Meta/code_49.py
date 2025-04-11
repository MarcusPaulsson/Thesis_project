def find_kth_digit(k):
    digit_length = 1
    count = 9
    start = 1

    # Determine the range where the k-th digit lies
    while k > digit_length * count:
        k -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    # Find the actual number containing the k-th digit
    start += (k - 1) // digit_length
    number_str = str(start)
    
    # Find the specific digit
    digit_index = (k - 1) % digit_length
    return number_str[digit_index]

# Read input
k = int(input().strip())
# Output the k-th digit
print(find_kth_digit(k))