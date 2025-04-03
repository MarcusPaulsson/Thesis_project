def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))

    a.sort()
    w.sort()

    happiness = 0
    
    # Assign largest numbers to friends with w[i] == 1
    l = n - 1
    for i in range(k):
        if w[i] == 1:
            happiness += 2 * a[l]
            l -= 1
    
    # Assign smallest numbers to friends with w[i] > 1
    r = 0
    for i in range(k - 1, -1, -1):
        if w[i] > 1:
            happiness += a[l] + a[r]
            l -= 1
            r += w[i] - 1
    
    print(happiness)


t = int(input())
for _ in range(t):
    solve()