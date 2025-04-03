def can_run_same_track(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between barriers for Kefa
    kefa_gaps = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    # Calculate the distances between barriers for Sasha
    sasha_gaps = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if kefa_gaps can be rotated to match sasha_gaps
    sasha_gaps_doubled = sasha_gaps + sasha_gaps  # Double the gaps to handle rotation
    for i in range(n):
        if kefa_gaps == sasha_gaps_doubled[i:i+n]:
            return "YES"
    
    return "NO"

# Input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output
print(can_run_same_track(n, L, kefa_distances, sasha_distances))