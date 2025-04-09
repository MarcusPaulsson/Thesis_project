def can_match_tracks(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between consecutive barriers for Kefa
    kefa_distances.append(kefa_distances[0] + L)  # Adding wrap-around distance
    kefa_intervals = [(kefa_distances[i] - kefa_distances[i-1]) % L for i in range(1, n+1)]

    # Calculate the distances between consecutive barriers for Sasha
    sasha_distances.append(sasha_distances[0] + L)  # Adding wrap-around distance
    sasha_intervals = [(sasha_distances[i] - sasha_distances[i-1]) % L for i in range(1, n+1)]

    # Check if Kefa's intervals can be aligned with Sasha's intervals
    for i in range(n):
        if kefa_intervals == sasha_intervals[i:] + sasha_intervals[:i]:
            return "YES"
    
    return "NO"

# Read input values
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Print result
print(can_match_tracks(n, L, kefa_distances, sasha_distances))