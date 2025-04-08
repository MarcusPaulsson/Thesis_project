def count_set_bits(n: int) -> int:
    """Count the number of set bits (1s) in the binary representation of a number."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def main():
    a = int(input("Enter an integer (1 ≤ a ≤ 64): ").strip())
    if 1 <= a <= 64:
        result = count_set_bits(a)
        print(result)
    else:
        print("Input must be between 1 and 64.")

if __name__ == "__main__":
    main()