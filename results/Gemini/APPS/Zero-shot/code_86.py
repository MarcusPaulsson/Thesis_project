def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    diff = n - sum(a)

    add = diff // k
    rem = diff % k

    for i in range(k):
        a[i] += add

    for i in range(k - 1, k - 1 - rem, -1):
        a[i] += 1

    for i in range(k - 1):
        if a[i + 1] > 2 * a[i]:
            needed = a[i + 1] - 2 * a[i]
            a[i] += needed
            a[i + 1] -= needed
            
            
            if a[i+1] <= a[i]:
                print("NO")
                return

    for i in range(k - 1):
        if a[i+1] <= a[i]:
            print("NO")
            return

    
    for i in range(k - 1):
        if a[i+1] > 2 * a[i]:
            print("NO")
            return

    if sum(a) != n:
        print("NO")
        return

    
    print("YES")
    print(*a)

solve()