def can_tracks_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the differences (gaps) between consecutive barriers and wrap around
    kefa_gaps = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_gaps = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Double the gaps for Kefa to handle circular comparison
    doubled_kefa_gaps = kefa_gaps * 2
    
    # Check if sasha_gaps is a contiguous subsequence in doubled_kefa_gaps
    for start in range(n):
        if doubled_kefa_gaps[start:start + n] == sasha_gaps:
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_tracks_coincide(n, L, kefa_distances, sasha_distances))