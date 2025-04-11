def find_integers(x):
    # Iterate through possible values for a and b
    for a in range(1, 11):
        for b in range(1, 11):
            # Check if the product of a and b is approximately equal to x
            if abs(a * b - x) < 1e-6:  # Using a small epsilon for floating-point comparison
                return a, b

def main():
    # Read input
    x = float(input().strip())
    
    # Get the result
    result = find_integers(x)
    
    # Print the output
    print(result[0], result[1])

if __name__ == "__main__":
    main()