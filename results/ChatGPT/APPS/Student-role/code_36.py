n = int(input())
a = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

# Calculate prefix sums to determine the ranges of worm labels in each pile
prefix_sums = [0] * n
prefix_sums[0] = a[0]
for i in range(1, n):
    prefix_sums[i] = prefix_sums[i - 1] + a[i]

# For each query, determine which pile it belongs to
results = []
for query in queries:
    # Binary search for the correct pile
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if prefix_sums[mid] < query:
            low = mid + 1
        else:
            high = mid
    results.append(low + 1)

# Print the results
print('\n'.join(map(str, results)))