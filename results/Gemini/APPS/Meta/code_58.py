def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    for x in counts:
        if counts[x] > k:
            print("NO")
            return

    coloring = [0] * n
    color_assignment = {}
    color_index = 1

    for i in range(n):
        num = a[i]
        if num not in color_assignment:
            color_assignment[num] = []

        if len(color_assignment[num]) < k:
            coloring[i] = color_index
            color_assignment[num].append(color_index)
            color_index = (color_index % k) + 1

    
    color_counts = [0] * (k + 1)
    for c in coloring:
        color_counts[c] += 1

    for i in range(1, k + 1):
        if color_counts[i] == 0:
            print("NO")
            return

    print("YES")
    print(*coloring)

solve()