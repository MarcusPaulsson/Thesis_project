def count_set_bits(n: int) -> int:
    """Return the number of set bits (1s) in the binary representation of n."""
    return bin(n).count('1')

def main():
    a = int(input("Enter an integer (1 ≤ a ≤ 64): "))
    if 1 <= a <= 64:
        print(count_set_bits(a))
    else:
        print("Input must be between 1 and 64.")

if __name__ == "__main__":
    main()