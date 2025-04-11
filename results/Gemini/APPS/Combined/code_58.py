def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1

    possible = True
    for x in counts:
        if counts[x] > k:
            possible = False
            break

    if not possible:
        print("NO")
        return

    colors = [0] * n
    color_index = 1

    for i in range(n):
        colors[i] = color_index
        color_index = (color_index % k) + 1
        if color_index == 0:
            color_index = k

    print("YES")
    print(*colors)

solve()