def solve():
    n, q = map(int, input().split())
    painters = []
    for _ in range(q):
        l, r = map(int, input().split())
        painters.append((l, r))

    max_painted = 0
    for i in range(q):
        for j in range(i + 1, q):
            
            chosen_painters = []
            for k in range(q):
                if k != i and k != j:
                    chosen_painters.append(painters[k])

            painted_sections = [0] * (n + 1)
            for l, r in chosen_painters:
                for section in range(l, r + 1):
                    painted_sections[section] = 1

            max_painted = max(max_painted, sum(painted_sections))

    print(max_painted)

solve()