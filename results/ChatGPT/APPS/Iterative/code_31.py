from math import gcd

def birthday_paradox(n, k):
    days = 1 << n  # This is 2^n
    if k > days:
        return 1, 1  # Guaranteed collision

    # Calculate the probability of no collision
    no_collision_num = 1
    for i in range(k):
        no_collision_num *= (days - i)

    no_collision_den = days ** k

    # The probability of at least one collision
    collision_num = no_collision_den - no_collision_num
    collision_den = no_collision_den

    # Reduce the fraction
    common_divisor = gcd(collision_num, collision_den)
    A = collision_num // common_divisor
    B = collision_den // common_divisor

    # Take modulo
    MOD = 10**6 + 3
    A %= MOD
    B %= MOD

    # Ensure A and B are coprime after modulo
    if gcd(A, B) != 1:
        raise ValueError("A and B are not coprime after modulo.")

    return A, B

def main():
    # Read input and validate
    try:
        n, k = map(int, input("Enter n and k separated by space: ").split())
        if n < 1 or k < 1:
            raise ValueError("n and k must be positive integers.")
    except ValueError as e:
        print(f"Input error: {e}")
        return

    A, B = birthday_paradox(n, k)
    print(A, B)

if __name__ == "__main__":
    main()