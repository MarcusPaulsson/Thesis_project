def can_coincide_tracks(n, L, kefa_distances, sasha_distances):
    def calculate_distances(distances):
        return [(distances[i] - distances[i - 1]) % L for i in range(1, n)] + [(distances[0] + L - distances[-1]) % L]

    kefa_diffs = calculate_distances(kefa_distances)
    sasha_diffs = calculate_distances(sasha_distances)

    # Check if any rotation of Kefa's distances matches Sasha's distances
    # We can use string manipulation for easier rotation comparison
    kefa_str = ' '.join(map(str, kefa_diffs))
    sasha_str = ' '.join(map(str, sasha_diffs * 2))  # double the Sasha's distances for rotation

    return "YES" if kefa_str in sasha_str else "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_coincide_tracks(n, L, kefa_distances, sasha_distances))