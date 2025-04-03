def kth_largest_in_multiplication_table(n, m, k):
    low, high = 1, n * m

    while low < high:
        mid = (low + high) // 2
        count = 0

        for i in range(1, n + 1):
            count += min(mid // i, m)

        if count < k:
            low = mid + 1
        else:
            high = mid

    return low

# Read input
n, m, k = map(int, input().split())
# Get the k-th largest number
result = kth_largest_in_multiplication_table(n, m, k)
# Print the result
print(result)