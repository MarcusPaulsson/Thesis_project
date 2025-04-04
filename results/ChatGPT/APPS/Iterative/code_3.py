from itertools import combinations

n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

max_painted = 0

for comb in combinations(range(q), q - 2):
    painted_sections = set()
    for i in comb:
        l, r = painters[i]
        painted_sections.update(range(l, r + 1))
    max_painted = max(max_painted, len(painted_sections))

print(max_painted)