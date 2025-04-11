def calculate_output(a: int) -> int:
    """Calculate the bit length of (a - 1)."""
    return (a - 1).bit_length()

def main():
    a = int(input().strip())
    if 1 <= a <= 64:
        print(calculate_output(a))
    else:
        raise ValueError("Input must be between 1 and 64 inclusive.")

if __name__ == "__main__":
    main()