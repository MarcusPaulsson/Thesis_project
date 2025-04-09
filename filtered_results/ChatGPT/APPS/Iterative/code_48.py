def kth_largest_in_multiplication_table(n, m, k):
    low, high = 1, n * m

    while low < high:
        mid = (low + high) // 2
        count = sum(min(mid // i, m) for i in range(1, n + 1))

        if count < k:
            low = mid + 1
        else:
            high = mid

    return low

# Read input
n, m, k = map(int, input().split())
# Get the k-th largest number in the multiplication table
result = kth_largest_in_multiplication_table(n, m, k)
# Print the result
print(result)