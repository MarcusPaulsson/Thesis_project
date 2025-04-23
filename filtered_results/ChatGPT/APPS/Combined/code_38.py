def can_coincide_tracks(n, L, kefa_distances, sasha_distances):
    # Calculate the differences between consecutive barriers for Kefa and Sasha
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if sasha_diffs can be obtained by rotating kefa_diffs
    double_kefa_diffs = kefa_diffs * 2  # Create a doubled list for easy rotation check
    for i in range(n):
        if double_kefa_diffs[i:i + n] == sasha_diffs:
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_coincide_tracks(n, L, kefa_distances, sasha_distances))