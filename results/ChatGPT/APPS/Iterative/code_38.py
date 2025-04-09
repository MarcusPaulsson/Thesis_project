def can_be_same_track(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between barriers for Kefa and Sasha
    kefa_diffs = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_diffs = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Check if sasha_diffs can be found in the doubled kefa_diffs
    combined_diffs = kefa_diffs * 2  # Concatenate to allow rotation
    for i in range(n):
        if combined_diffs[i:i + n] == sasha_diffs:
            return "YES"
    return "NO"

# Read input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Get result and print
result = can_be_same_track(n, L, kefa_distances, sasha_distances)
print(result)