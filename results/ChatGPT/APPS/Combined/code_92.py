def find_integers(x):
    # Iterate over possible integer pairs (a, b) where 1 <= a, b <= 10
    for a in range(1, 11):
        for b in range(1, 11):
            # Calculate the value of a * b / (a + b) and compare with x
            if abs(a * b / (a + b) - x) < 1e-6:  # Tolerance for floating-point comparison
                return a, b

def main():
    # Read input
    x = float(input().strip())
    
    # Find integers
    a, b = find_integers(x)
    
    # Print output
    print(a, b)

if __name__ == "__main__":
    main()