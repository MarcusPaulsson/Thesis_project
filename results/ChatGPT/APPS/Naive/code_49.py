def find_kth_digit(k):
    length = 1
    count = 9
    start = 1
    
    # Determine the range where the k-th digit falls
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10
    
    # Find the exact number containing the k-th digit
    start += (k - 1) // length
    num_str = str(start)
    
    # Find the exact digit
    digit_index = (k - 1) % length
    return num_str[digit_index]

# Input
k = int(input())
# Output
print(find_kth_digit(k))