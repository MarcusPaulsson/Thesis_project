def find_pile(n, piles, m, queries):
    # Create a prefix sum array for the pile ranges
    prefix_sum = [0] * n
    prefix_sum[0] = piles[0]
    
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + piles[i]
    
    result = []
    for query in queries:
        # Binary search to find the correct pile
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if prefix_sum[mid] < query:
                low = mid + 1
            else:
                high = mid
        result.append(low + 1)  # Piles are 1-indexed

    return result

# Input handling
n = int(input())
piles = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

# Get the results
results = find_pile(n, piles, m, queries)

# Print the results
for res in results:
    print(res)