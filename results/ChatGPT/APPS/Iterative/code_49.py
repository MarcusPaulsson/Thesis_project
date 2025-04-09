def find_kth_digit(k):
    length = 1
    count = 9
    start = 1
    
    # Determine the range in which the k-th digit resides
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10
    
    # Calculate the actual number containing the k-th digit
    start += (k - 1) // length
    num_str = str(start)
    
    # Return the specific digit from the number
    return int(num_str[(k - 1) % length])

k = int(input().strip())
print(find_kth_digit(k))