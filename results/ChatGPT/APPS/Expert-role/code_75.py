import math

def min_square_side_length(n):
    # The formula derived for the minimum square side length for a 2n-gon
    return 2 * math.sin(math.pi / (2 * n))

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        side_length = min_square_side_length(n)
        results.append(f"{side_length:.9f}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()