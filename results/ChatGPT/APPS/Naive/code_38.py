def can_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between consecutive barriers for Kefa and Sasha
    kefa_gaps = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_gaps = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Double the kefa_gaps to account for circular shifts
    kefa_gaps_doubled = kefa_gaps * 2
    
    # Check if sasha_gaps can be found in the doubled kefa_gaps
    for i in range(n):
        if kefa_gaps_doubled[i:i + n] == sasha_gaps:
            return "YES"
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output the result
print(can_coincide(n, L, kefa_distances, sasha_distances))