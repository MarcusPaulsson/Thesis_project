def max_chocolates(n, a, b, p, q):
    from math import gcd
    
    count_a = n // a
    count_b = n // b
    lcm_ab = (a * b) // gcd(a, b)  # Least common multiple of a and b
    count_ab = n // lcm_ab  # count of indices divisible by both a and b

    # Calculate number of chocolates
    chocolates_option1 = (count_a * p) + ((count_b - count_ab) * q)
    chocolates_option2 = (count_b * q) + ((count_a - count_ab) * p)

    return max(chocolates_option1, chocolates_option2)

# Read input safely
try:
    n, a, b, p, q = map(int, input("Enter values for n, a, b, p, q separated by spaces: ").split())
    if n < 0 or a <= 0 or b <= 0 or p < 0 or q < 0:
        raise ValueError("n must be non-negative and a, b must be positive; p and q must be non-negative.")
    print(max_chocolates(n, a, b, p, q))
except ValueError as e:
    print("Invalid input:", e)