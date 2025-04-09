def solve():
    n, q = map(int, input().split())
    painters = []
    for _ in range(q):
        painters.append(tuple(map(int, input().split())))

    def calculate_painted_sections(selected_painters):
        painted = [False] * n
        for l, r in selected_painters:
            for i in range(l - 1, r):
                painted[i] = True
        return sum(painted)

    max_painted = 0
    for i in range(q):
        for j in range(i + 1, q):
            selected_painters = []
            for k in range(q):
                if k != i and k != j:
                    selected_painters.append(painters[k])
            max_painted = max(max_painted, calculate_painted_sections(selected_painters))

    print(max_painted)

solve()