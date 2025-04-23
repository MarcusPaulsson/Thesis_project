def solve():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))

    total_length = sum(c)
    min_empty = n - total_length

    if min_empty > (m * (d - 1)):
        print("NO")
        return

    arr = [0] * n
    pos = 0
    
    for i in range(m):
        needed_empty = d - 1
        empty_before = min(min_empty, needed_empty)
        
        pos += empty_before
        min_empty -= empty_before
        
        for j in range(c[i]):
            arr[pos] = i + 1
            pos += 1

    for i in range(n):
        if arr[i] == 0:
            continue
        
    print("YES")
    print(*arr)

solve()