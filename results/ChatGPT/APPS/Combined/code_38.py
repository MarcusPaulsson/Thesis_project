def can_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the gaps between consecutive barriers for both Kefa and Sasha
    kefa_gaps = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_gaps = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Double the Kefa gaps to facilitate rotation comparison
    doubled_kefa_gaps = kefa_gaps * 2
    
    # Check if Sasha's gaps can be found in the doubled Kefa gaps
    for i in range(n):
        if doubled_kefa_gaps[i:i+n] == sasha_gaps:
            return "YES"
    
    return "NO"

# Read input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_coincide(n, L, kefa_distances, sasha_distances))