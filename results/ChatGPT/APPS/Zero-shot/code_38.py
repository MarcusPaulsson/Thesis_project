def can_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between consecutive barriers for Kefa and Sasha
    kefa_intervals = [(kefa_distances[i] - kefa_distances[i - 1]) % L for i in range(1, n)]
    kefa_intervals.append((kefa_distances[0] + L - kefa_distances[-1]) % L)
    
    sasha_intervals = [(sasha_distances[i] - sasha_distances[i - 1]) % L for i in range(1, n)]
    sasha_intervals.append((sasha_distances[0] + L - sasha_distances[-1]) % L)
    
    # Check if kefa_intervals can be rotated to match sasha_intervals
    double_kefa_intervals = kefa_intervals * 2
    for i in range(n):
        if double_kefa_intervals[i:i+n] == sasha_intervals:
            return "YES"
    
    return "NO"

# Read input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Get result and print
result = can_coincide(n, L, kefa_distances, sasha_distances)
print(result)