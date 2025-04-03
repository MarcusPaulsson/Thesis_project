def find_kth_digit(k):
    length = 1
    count = 9
    start = 1

    # Determine the length of the number that contains the k-th digit
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10

    # Find the actual number that contains the k-th digit
    start += (k - 1) // length
    num_str = str(start)
    
    # Find the specific digit
    digit_index = (k - 1) % length
    return num_str[digit_index]

k = int(input())
print(find_kth_digit(k))