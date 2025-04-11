def can_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between consecutive barriers for Kefa
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    # Calculate the distances between consecutive barriers for Sasha
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if kefa_diffs can be rotated to match sasha_diffs
    for i in range(n):
        if kefa_diffs == sasha_diffs[i:] + sasha_diffs[:i]:
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output result
print(can_coincide(n, L, kefa_distances, sasha_distances))