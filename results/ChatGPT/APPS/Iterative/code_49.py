def find_kth_digit(k):
    if k <= 0:
        raise ValueError("k must be a positive integer.")

    length = 1
    count = 9
    start = 1

    # Determine the range where the k-th digit falls
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10

    # Find the actual number that contains the k-th digit
    start += (k - 1) // length
    number = str(start)
    
    # Find the specific digit
    digit_index = (k - 1) % length
    return number[digit_index]

try:
    k = int(input("Enter a positive integer k: "))
    print(find_kth_digit(k))
except ValueError as e:
    print(e)