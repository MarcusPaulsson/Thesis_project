import math

def min_square_side_length(n):
    # The formula derived for the minimum square side length to embed a 2n-gon
    return math.sqrt(2) * (math.cos(math.pi / (2 * n)) / math.sin(math.pi / (2 * n)))

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