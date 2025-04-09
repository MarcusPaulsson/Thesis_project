def solve():
    """
    Calculates the minimum possible absolute difference between the sums of two sets
    formed by dividing the sequence 1, 2, ..., n.

    The problem is equivalent to finding the minimum possible value of |sum(A) - sum(B)|,
    where A and B are two sets that partition the sequence 1, 2, ..., n.

    The sum of the sequence 1, 2, ..., n is given by n * (n + 1) // 2.
    If this sum is even, it's possible to divide the sequence into two sets with equal sums,
    resulting in a difference of 0. Otherwise, the minimum possible difference is 1.
    """
    n = int(input())
    total_sum = n * (n + 1) // 2
    print(total_sum % 2)

solve()