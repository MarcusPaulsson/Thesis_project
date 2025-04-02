for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [-1] * (n+1)
    for k in range(1, n+1):
        d = {}
        for i in range(0, n-k+1):
            subarr = arr[i:i+k]
            d[min(subarr)] = True
        if len(d) == k:
            ans[k] = min(d)
    print(*ans)