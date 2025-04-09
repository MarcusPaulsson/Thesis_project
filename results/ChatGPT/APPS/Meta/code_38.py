def can_tracks_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the differences for Kefa's barriers
    kefa_diffs = [(kefa_distances[i] - kefa_distances[i - 1]) % L for i in range(1, n)]
    kefa_diffs.append((kefa_distances[0] + L - kefa_distances[-1]) % L)  # Closing the circle

    # Calculate the differences for Sasha's barriers
    sasha_diffs = [(sasha_distances[i] - sasha_distances[i - 1]) % L for i in range(1, n)]
    sasha_diffs.append((sasha_distances[0] + L - sasha_distances[-1]) % L)  # Closing the circle

    # Check if any rotation of Kefa's differences matches Sasha's differences
    doubled_kefa_diffs = kefa_diffs + kefa_diffs

    for i in range(n):
        if doubled_kefa_diffs[i:i+n] == sasha_diffs:
            return "YES"
    
    return "NO"

# Reading input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output result
print(can_tracks_coincide(n, L, kefa_distances, sasha_distances))