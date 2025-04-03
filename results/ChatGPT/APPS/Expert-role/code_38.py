def can_run_same_track(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between barriers for Kefa
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    # Calculate the distances between barriers for Sasha
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if Kefa's distances can be rotated to match Sasha's distances
    doubled_kefa_diffs = kefa_diffs * 2
    for i in range(n):
        if doubled_kefa_diffs[i:i+n] == sasha_diffs:
            return "YES"
    
    return "NO"

# Read input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_run_same_track(n, L, kefa_distances, sasha_distances))