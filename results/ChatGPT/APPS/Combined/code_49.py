def find_kth_digit(k):
    length = 1  # The current digit length (1 for 1-9, 2 for 10-99, etc.)
    count = 9   # The count of numbers with the current digit length
    start = 1   # The starting number with the current digit length

    # Determine the range in which the k-th digit falls
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10

    # Find the actual number that contains the k-th digit
    start += (k - 1) // length
    number_str = str(start)
    
    # Find the specific digit in that number
    return number_str[(k - 1) % length]

if __name__ == "__main__":
    # Read input
    k = int(input().strip())
    # Print the k-th digit
    print(find_kth_digit(k))