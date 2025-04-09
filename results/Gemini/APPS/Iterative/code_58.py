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
    color = 1
    
    for i in range(n):
        coloring[i] = color
        color = (color % k) + 1

    print("YES")
    print(*coloring)

solve()