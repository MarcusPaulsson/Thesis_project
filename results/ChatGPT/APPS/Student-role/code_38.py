def can_be_same_track(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between consecutive barriers for Kefa and Sasha
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if Kefa's differences can match Sasha's differences by rotation
    for start in range(n):
        if all(kefa_diffs[i] == sasha_diffs[(i + start) % n] for i in range(n)):
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_be_same_track(n, L, kefa_distances, sasha_distances))