def can_match_tracks(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between barriers for Kefa and Sasha
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Double the Kefa's differences to account for circular matching
    kefa_diffs_extended = kefa_diffs + kefa_diffs
    
    # Check if Sasha's differences can be found in the extended Kefa's differences
    for start in range(n):
        if kefa_diffs_extended[start:start + n] == sasha_diffs:
            return "YES"
    
    return "NO"

# Reading input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_match_tracks(n, L, kefa_distances, sasha_distances))