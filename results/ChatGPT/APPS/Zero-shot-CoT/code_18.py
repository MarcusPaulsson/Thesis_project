import math

def minimum_square_size(n):
    # The length of the side of the square needed to embed the 2n-gon
    # is derived using the formula: 2 * (1 + sin(π/n))
    return math.sqrt(2) * (1 + math.sin(math.pi / n))

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        result = minimum_square_size(n)
        results.append(f"{result:.9f}")
    print("\n".join(results))

if __name__ == "__main__":
    main()