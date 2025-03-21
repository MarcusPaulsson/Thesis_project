import math

def min_square_side_length(n):
    # Calculate the minimum square side length required to embed a 2n-gon
    angle = math.pi / n
    # The formula derived is side_length = 2 * sin(angle) / cos(angle / 2)
    side_length = 2 * math.sin(angle) / math.cos(angle / 2)
    return side_length

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