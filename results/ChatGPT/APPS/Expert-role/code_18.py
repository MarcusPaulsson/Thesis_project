import math

def minimum_square_side_length(n):
    # For a 2n-gon, the minimum square side length required to embed it
    # can be calculated using the formula derived from the geometry of the situation.
    return math.sqrt(2) * n / math.sin(math.pi / (2 * n))

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        result = minimum_square_side_length(n)
        results.append(f"{result:.9f}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()