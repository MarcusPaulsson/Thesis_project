n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Normalize distances for Kefa and Sasha
def normalize(distances):
    normalized = []
    for i in range(n):
        normalized.append((distances[i] - distances[0]) % L)
    return normalized

kefa_normalized = normalize(kefa_distances)
sasha_normalized = normalize(sasha_distances)

# Check if Kefa's normalized distances match Sasha's normalized distances in any circular permutation
def can_match(kefa, sasha):
    double_kefa = kefa + kefa
    sasha_length = len(sasha)
    for i in range(len(kefa)):
        if double_kefa[i:i+sasha_length] == sasha:
            return True
    return False

if can_match(kefa_normalized, sasha_normalized):
    print("YES")
else:
    print("NO")