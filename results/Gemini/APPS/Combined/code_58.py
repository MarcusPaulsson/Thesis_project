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

    colors = [0] * n
    color_idx = 1

    for i in range(n):
        colors[i] = color_idx
        color_idx = (color_idx % k) + 1
        if color_idx == 0:
            color_idx = 1

    print("YES")
    print(*colors)

solve()