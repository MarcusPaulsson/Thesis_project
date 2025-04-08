def find_kth_digit(k):
    length = 1  # Starting with 1-digit numbers
    count = 9   # There are 9 one-digit numbers
    start = 1   # The first one-digit number is 1

    # Determine the length of the number that contains the k-th digit
    while k > length * count:
        k -= length * count
        length += 1
        count *= 10
        start *= 10

    # Find the exact number that contains the k-th digit
    start += (k - 1) // length
    num_str = str(start)
    
    # Find the digit's position in that number
    digit_index = (k - 1) % length
    return num_str[digit_index]

if __name__ == "__main__":
    k = int(input().strip())
    print(find_kth_digit(k))