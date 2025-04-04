def can_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the differences (gaps) between consecutive barriers for Kefa and Sasha
    kefa_gaps = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    sasha_gaps = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Create a doubled list of Sasha's gaps to account for circular shifts
    doubled_sasha_gaps = sasha_gaps * 2
    
    # Check if Kefa's gaps are a contiguous subsequence in the doubled Sasha's gaps
    if any(kefa_gaps == doubled_sasha_gaps[i:i + n] for i in range(n)):
        return "YES"
    
    return "NO"

# Read input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Get the result and print it
result = can_coincide(n, L, kefa_distances, sasha_distances)
print(result)