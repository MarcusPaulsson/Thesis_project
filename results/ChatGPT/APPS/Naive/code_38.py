def can_tracks_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between barriers for Kefa and Sasha
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Double the Sasha's differences to handle circular matching
    sasha_diffs_extended = sasha_diffs + sasha_diffs

    # Check if Kefa's differences exist as a contiguous subsequence in the extended Sasha's differences
    for i in range(n):
        if kefa_diffs == sasha_diffs_extended[i:i+n]:
            return "YES"
    
    return "NO"

# Input handling
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_tracks_coincide(n, L, kefa_distances, sasha_distances))