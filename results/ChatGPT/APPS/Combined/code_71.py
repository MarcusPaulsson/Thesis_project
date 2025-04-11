def calculate_output(a: int) -> int:
    """Calculate the output based on the input integer a."""
    return (a - 1).bit_length()

def main():
    # Read input
    a = int(input().strip())
    # Output the result
    print(calculate_output(a))

if __name__ == "__main__":
    main()