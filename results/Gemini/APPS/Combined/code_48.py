def solve():
    n, m, k = map(int, input().split())

    def count_smaller_equal(x):
        """
        Counts the number of elements in the n x m multiplication table that are less than or equal to x.
        """
        count = 0
        for i in range(1, n + 1):
            count += min(m, x // i)
        return count

    # Binary search for the k-th largest number
    left, right = 1, n * m
    
    while left <= right:
        mid = (left + right) // 2
        
        if count_smaller_equal(mid) >= k:
            right = mid - 1
        else:
            left = mid + 1
            
    print(left)

solve()