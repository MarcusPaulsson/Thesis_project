# Read number of piles
n = int(input().strip())

# Read the number of worms in each pile
a = list(map(int, input().strip().split()))

# Read number of juicy worms
m = int(input().strip())

# Read the labels of juicy worms
q = list(map(int, input().strip().split()))

# Create a prefix sum array to determine the ranges of each pile
prefix_sum = [0] * n
prefix_sum[0] = a[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + a[i]

# For each query, determine the pile number
result = []
for worm in q:
    # We can use binary search to find the correct pile
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if prefix_sum[mid] < worm:
            low = mid + 1
        else:
            high = mid
    result.append(low + 1)  # Convert 0-index to 1-index

# Print results
print("\n".join(map(str, result)))