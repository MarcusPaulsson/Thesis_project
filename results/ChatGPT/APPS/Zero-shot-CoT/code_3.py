n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

# We will calculate the painted sections for every combination of q-2 painters
def painted_sections(painters):
    painted = [0] * (n + 1)
    for l, r in painters:
        for i in range(l, r + 1):
            painted[i] = 1
    return sum(painted)

max_painted = 0

# Try all combinations of q-2 painters
from itertools import combinations

for comb in combinations(painters, q - 2):
    max_painted = max(max_painted, painted_sections(comb))

print(max_painted)