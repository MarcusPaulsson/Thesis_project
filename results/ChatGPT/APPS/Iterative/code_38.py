def can_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between consecutive barriers for Kefa and Sasha
    kefa_gaps = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_gaps = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]

    # Check if Sasha's gaps can be obtained from Kefa's gaps by rotation
    double_kefa_gaps = kefa_gaps * 2  # Concatenate Kefa's gaps with itself

    # Check for a matching segment of length n in the doubled gaps
    for i in range(n):
        if double_kefa_gaps[i:i + n] == sasha_gaps:
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output result
print(can_coincide(n, L, kefa_distances, sasha_distances))