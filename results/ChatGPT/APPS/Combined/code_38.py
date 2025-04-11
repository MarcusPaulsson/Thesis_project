def can_coincide_tracks(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between consecutive barriers for Kefa
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    # Calculate the distances between consecutive barriers for Sasha
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if the two lists of differences can match by rotation
    double_kefa_diffs = kefa_diffs * 2  # Concatenate to allow rotation matching
    return "YES" if any(double_kefa_diffs[i:i + n] == sasha_diffs for i in range(n)) else "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_coincide_tracks(n, L, kefa_distances, sasha_distances))