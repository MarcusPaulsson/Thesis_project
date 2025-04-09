def can_tracks_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between barriers for Kefa and Sasha
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if Sasha's differences can match Kefa's differences by cyclic rotation
    double_kefa_diffs = kefa_diffs + kefa_diffs
    
    for i in range(n):
        if double_kefa_diffs[i:i + n] == sasha_diffs:
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_tracks_coincide(n, L, kefa_distances, sasha_distances))