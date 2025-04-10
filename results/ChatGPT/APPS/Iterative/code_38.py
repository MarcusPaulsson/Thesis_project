def can_be_same_track(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between consecutive barriers for Kefa
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    # Calculate the distances between consecutive barriers for Sasha
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if kefa_diffs can be rotated to match sasha_diffs
    double_kefa_diffs = kefa_diffs * 2
    
    # Use slicing to check for a match
    for i in range(n):
        if double_kefa_diffs[i:i+n] == sasha_diffs:
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_be_same_track(n, L, kefa_distances, sasha_distances))