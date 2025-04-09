def count_set_bits(number: int) -> int:
    """Returns the count of set bits (1s) in the binary representation of the given number."""
    count = 0

    while number:
        count += number & 1  # Increment count if the last bit is set
        number >>= 1  # Right shift to check the next bit

    return count

def main():
    # Read input and ensure it is within the required range
    a = int(input().strip())
    if 1 <= a <= 64:
        print(count_set_bits(a))
    else:
        raise ValueError("Input must be between 1 and 64 inclusive.")

if __name__ == "__main__":
    main()