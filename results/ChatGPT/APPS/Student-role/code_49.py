def find_kth_digit(k):
    length = 1
    count = 9
    start = 1

    # Determine the range where the k-th digit lies
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10

    # Find the actual number containing the k-th digit
    start += (k - 1) // length
    num_str = str(start)
    
    # Find the digit
    return num_str[(k - 1) % length]

k = int(input())
print(find_kth_digit(k))