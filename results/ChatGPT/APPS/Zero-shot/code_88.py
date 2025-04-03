def can_tracks_coincide(n, L, kefa_distances, sasha_distances):
    # Calculate the distances between barriers for Kefa
    kefa_intervals = [(kefa_distances[(i + 1) % n] - kefa_distances[i]) % L for i in range(n)]
    # Calculate the distances between barriers for Sasha
    sasha_intervals = [(sasha_distances[(i + 1) % n] - sasha_distances[i]) % L for i in range(n)]
    
    # Function to check if one list is a rotation of another
    def is_rotation(lst1, lst2):
        return len(lst1) == len(lst2) and any(lst1 == lst2[i:] + lst2[:i] for i in range(len(lst2)))
    
    # Check if Kefa's intervals are a rotation of Sasha's intervals
    if is_rotation(kefa_intervals, sasha_intervals):
        print("YES")
    else:
        print("NO")

# Read input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Check if the tracks coincide
can_tracks_coincide(n, L, kefa_distances, sasha_distances)