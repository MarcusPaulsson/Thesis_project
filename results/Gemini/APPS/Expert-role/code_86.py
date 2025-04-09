def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [0] * k
    for i in range(k):
        a[i] = i + 1

    remaining = n - k * (k + 1) // 2
    
    base = remaining // k
    rem = remaining % k
    
    for i in range(k):
        a[i] += base
    
    for i in range(k - 1, k - 1 - rem, -1):
        a[i] += 1
        
    for i in range(k - 1):
        if a[i+1] > 2 * a[i]:
            diff = a[i+1] - 2 * a[i]
            a[i+1] -= diff
            a[k-1] += diff
    
    
    valid = True
    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            valid = False
            break
            
    if min(a) <= 0:
        valid = False

    if sum(a) != n:
        valid = False

    if valid:
        print("YES")
        print(*a)
    else:
        print("NO")

solve()