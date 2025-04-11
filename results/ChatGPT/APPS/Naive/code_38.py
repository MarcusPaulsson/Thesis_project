def can_coincide_tracks(n, L, kefa_distances, sasha_distances):
    # Calculate the differences between consecutive barriers for both Kefa and Sasha
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Double the kefa_diffs to account for circular nature
    kefa_diffs_extended = kefa_diffs * 2
    
    # Check if sasha_diffs can be found in the extended kefa_diffs
    for i in range(n):
        if kefa_diffs_extended[i:i + n] == sasha_diffs:
            return "YES"
    
    return "NO"

# Read input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output result
print(can_coincide_tracks(n, L, kefa_distances, sasha_distances))