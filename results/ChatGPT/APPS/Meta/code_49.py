def find_kth_digit(k):
    digit_length = 1
    count = 9
    start = 1

    while k > digit_length * count:
        k -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    # Determine the actual number containing the k-th digit
    start += (k - 1) // digit_length
    number_str = str(start)
    
    # Find the specific digit
    digit_index = (k - 1) % digit_length
    return number_str[digit_index]

# Input reading
k = int(input())
print(find_kth_digit(k))