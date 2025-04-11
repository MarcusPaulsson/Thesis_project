def find_kth_digit(k):
    length = 1  # Current digit length
    count = 9   # Count of numbers with the current digit length
    start = 1   # Starting number with the current digit length

    # Determine the range where the k-th digit lies
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10

    # Find the actual number that contains the k-th digit
    start += (k - 1) // length
    num_str = str(start)
    
    # Find the specific digit
    return num_str[(k - 1) % length]

k = int(input().strip())
print(find_kth_digit(k))