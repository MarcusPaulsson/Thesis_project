n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

# Create a prefix sum array to determine the ranges of each pile
prefix_sum = [0] * n
prefix_sum[0] = a[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + a[i]

# For each query, determine which pile the worm belongs to
result = []
for worm in q:
    # Binary search to find the pile
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if prefix_sum[mid] < worm:
            low = mid + 1
        else:
            high = mid
    result.append(low + 1)  # +1 because we want 1-based index

# Print the results
print("\n".join(map(str, result)))