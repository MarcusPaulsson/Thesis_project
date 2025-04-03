def solve():
    n = int(input())
    a = list(map(int, input().split()))

    bounds = []
    for i in range(n):
        if a[i] == -1:
            if i > 0 and a[i-1] != -1:
                bounds.append(a[i-1])
            if i < n-1 and a[i+1] != -1:
                bounds.append(a[i+1])
    
    if not bounds:
        print(0, 42)
        return

    min_bound = min(bounds)
    max_bound = max(bounds)
    
    k = (min_bound + max_bound) // 2
    
    arr = []
    for x in a:
        if x == -1:
            arr.append(k)
        else:
            arr.append(x)
    
    m = 0
    for i in range(n-1):
        m = max(m, abs(arr[i] - arr[i+1]))
    
    print(m, k)


t = int(input())
for _ in range(t):
    solve()