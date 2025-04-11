def solve():
    n, q = map(int, input().split())
    painters = []
    for _ in range(q):
        painters.append(tuple(map(int, input().split())))

    max_painted = 0
    for i in range(q):
        for j in range(i + 1, q):
            
            hired_painters = []
            for k in range(q):
                if k != i and k != j:
                    hired_painters.append(painters[k])

            painted_sections = [0] * n
            for l, r in hired_painters:
                for section in range(l - 1, r):
                    painted_sections[section] = 1

            max_painted = max(max_painted, sum(painted_sections))

    print(max_painted)

solve()