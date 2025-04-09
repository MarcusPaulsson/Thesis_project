def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [0] * k
    for i in range(k):
        a[i] = i + 1

    remaining = n - k * (k + 1) // 2

    increase = remaining // k
    remaining %= k

    for i in range(k):
        a[i] += increase

    for i in range(k - 1, k - 1 - remaining, -1):
        a[i] += 1
    
    for i in range(k - 1):
        if a[i+1] > 2 * a[i]:
            diff = a[i+1] - 2 * a[i]
            a[i+1] -= diff
            a[k-1] += diff
            
            if a[i+1] > 2 * a[i]:
                print("NO")
                return

    for i in range(k - 1):
        if a[i+1] <= a[i]:
            print("NO")
            return
    

    print("YES")
    print(*a)

solve()