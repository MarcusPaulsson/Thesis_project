def solve():
    """
    Calculates the minimum possible absolute difference between the sums of two sets
    formed by dividing the sequence 1, 2, ..., n.

    The problem is equivalent to finding the minimum possible value of |sum(A) - sum(B)|,
    where A and B are two sets that partition the sequence 1, 2, ..., n.
    This is equivalent to finding the absolute difference between the total sum and twice the sum of one of the sets.
    The minimum value is achieved when the sum of one set is as close as possible to half the total sum.
    If the total sum is even, the minimum difference is 0.
    If the total sum is odd, the minimum difference is 1.

    The total sum of the sequence 1, 2, ..., n is n * (n + 1) // 2.
    """
    n = int(input())
    total_sum = n * (n + 1) // 2

    # If the total sum is even, the minimum difference is 0.
    # If the total sum is odd, the minimum difference is 1.
    print(total_sum % 2)

solve()