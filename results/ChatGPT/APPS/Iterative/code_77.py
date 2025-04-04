def min_difference(n):
    total_sum = n * (n + 1) // 2
    return total_sum % 2 != 0

try:
    n = int(input("Enter a positive integer: "))
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    print(min_difference(n))
except ValueError as e:
    print(f"Invalid input: {e}")