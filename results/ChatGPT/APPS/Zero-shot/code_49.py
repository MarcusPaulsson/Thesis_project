def find_kth_digit(k):
    length = 1  # Length of the numbers we are currently considering
    count = 9   # Count of numbers with the current length
    start = 1   # Starting number with the current length

    # Determine the length of the number that contains the k-th digit
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10

    # Determine the actual number that contains the k-th digit
    start += (k - 1) // length
    num_str = str(start)
    
    # Find the specific digit
    return num_str[(k - 1) % length]

# Read input
k = int(input().strip())
# Output the result
print(find_kth_digit(k))