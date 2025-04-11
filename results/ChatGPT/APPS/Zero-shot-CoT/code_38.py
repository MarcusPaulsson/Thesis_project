def can_be_same_track(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between barriers for Kefa and Sasha
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if sasha_diffs can be obtained by rotating kefa_diffs
    for i in range(n):
        if kefa_diffs[i:] + kefa_diffs[:i] == sasha_diffs:
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_be_same_track(n, L, kefa_distances, sasha_distances))