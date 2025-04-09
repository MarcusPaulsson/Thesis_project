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

    print("YES")

    colors = [0] * n
    color_index = 1
    
    for i in range(n):
        colors[i] = color_index
        color_index = (color_index % k) + 1
        if color_index == 0:
            color_index = 1

    print(*colors)

solve()