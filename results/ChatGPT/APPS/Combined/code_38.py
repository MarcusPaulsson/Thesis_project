def can_coincide_tracks(n, L, kefa_distances, sasha_distances):
    # Calculate the differences between consecutive barriers for both Kefa and Sasha
    kefa_gaps = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_gaps = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Double the sasha_gaps to handle the circular nature
    doubled_sasha_gaps = sasha_gaps * 2
    
    # Check if kefa_gaps can be found in doubled_sasha_gaps
    for i in range(n):
        if kefa_gaps == doubled_sasha_gaps[i:i+n]:
            return "YES"
    
    return "NO"

# Input processing
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Get the result and print
result = can_coincide_tracks(n, L, kefa_distances, sasha_distances)
print(result)