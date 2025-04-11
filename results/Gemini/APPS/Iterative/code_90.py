def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)

    if (m + 1) * (d - 1) + total_length < n:
        print("NO")
        return

    arr = [0] * n
    pos = 0
    
    for i in range(m):
        needed_empty = min(d - 1, n - pos - total_length)
        pos += needed_empty
        
        for j in range(c[i]):
            arr[pos] = i + 1
            pos += 1
        total_length -= c[i]

    print("YES")
    print(*arr)

solve()