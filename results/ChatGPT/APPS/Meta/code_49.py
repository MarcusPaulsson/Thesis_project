def find_kth_digit(k):
    # Initialize variables
    digit_length = 1  # Length of numbers (1 for 1-9, 2 for 10-99, etc.)
    count_of_numbers = 9  # Count of numbers with the current digit length
    current_range_start = 1  # Starting number in the current range

    # Find the range where the k-th digit falls
    while k > digit_length * count_of_numbers:
        k -= digit_length * count_of_numbers
        digit_length += 1
        count_of_numbers *= 10
        current_range_start *= 10

    # Find the actual number that contains the k-th digit
    number_index = (k - 1) // digit_length  # 0-based index of the number
    digit_index = (k - 1) % digit_length    # 0-based index of the digit

    actual_number = current_range_start + number_index
    return str(actual_number)[digit_index]

# Read input
k = int(input().strip())
# Print the k-th digit
print(find_kth_digit(k))