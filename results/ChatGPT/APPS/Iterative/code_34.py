def can_distribute(x, n, a, b):
    plates_for_a = (a + x - 1) // x  # Minimum plates needed for cake a
    plates_for_b = (b + x - 1) // x  # Minimum plates needed for cake b
    return plates_for_a + plates_for_b <= n

def max_min_pieces(n, a, b):
    left, right = 1, max(a, b)
    while left < right:
        mid = (left + right + 1) // 2
        if can_distribute(mid, n, a, b):
            left = mid
        else:
            right = mid - 1
    return left

def main():
    try:
        n, a, b = map(int, input("Enter n, a, b values separated by space: ").split())
        if n < 1 or a < 1 or b < 1:
            raise ValueError("All input values must be positive integers.")
        result = max_min_pieces(n, a, b)
        print(result)
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()