def solve():
    """
    Calculates the minimum possible absolute difference between the sums of two sets
    formed by dividing the sequence 1, 2, ..., n into two sets.

    The problem is equivalent to finding the parity of the sum of the sequence.
    If the sum is even, the minimum difference is 0.
    If the sum is odd, the minimum difference is 1.
    """
    n = int(input())
    total_sum = n * (n + 1) // 2  # Calculate the sum of the sequence
    print(total_sum % 2)  # Print the parity of the sum

solve()