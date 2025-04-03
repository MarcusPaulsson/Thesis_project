n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]

def count_painted(painters):
    painted = [0] * (n + 1)
    for l, r in painters:
        for i in range(l, r + 1):
            painted[i] = 1
    return sum(painted)

max_painted = 0

for i in range(q):
    for j in range(i + 1, q):
        remaining_painters = [painters[k] for k in range(q) if k != i and k != j]
        max_painted = max(max_painted, count_painted(remaining_painters))

print(max_painted)