def can_be_same_track(n, L, kefa_distances, sasha_distances):
    # Calculate the differences between consecutive barriers for both
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if we can find a rotation of kefa_diffs that matches sasha_diffs
    for i in range(n):
        # Rotate kefa_diffs by i positions
        rotated_kefa_diffs = kefa_diffs[i:] + kefa_diffs[:i]
        if rotated_kefa_diffs == sasha_diffs:
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output result
print(can_be_same_track(n, L, kefa_distances, sasha_distances))