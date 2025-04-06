def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    remaining = n - k * (k + 1) // 2

    for i in range(k):
        a[i] += remaining // k
    
    remaining %= k
    
    for i in range(k - 1, k - 1 - remaining, -1):
        a[i] += 1

    for i in range(k - 1):
        if a[i+1] <= a[i] or a[i+1] > 2 * a[i]:
            
            diff = a[i] + 1 - a[i+1]
            
            a[i+1] = a[i] + 1
            
            
            remaining = 0
            for j in range(i+1):
                remaining += a[j]
                
            required_sum = n - (sum(a[i+1:]))
            
            if required_sum < (i+1)*(i+2)//2:
                print("NO")
                return
            
            
            a = [j + 1 for j in range(k)]
            remaining = n - k * (k + 1) // 2

            for ii in range(k):
                a[ii] += remaining // k
            
            remaining %= k
            
            for ii in range(k - 1, k - 1 - remaining, -1):
                a[ii] += 1
                
            for ii in range(i):
                if a[ii+1] <= a[ii] or a[ii+1] > 2 * a[ii]:
                     print("NO")
                     return
                    
            for ii in range(i, k-1):
                if a[ii+1] <= a[ii] or a[ii+1] > 2 * a[ii]:
                     print("NO")
                     return
            
            
            
            
    for i in range(k - 1):
        if a[i+1] <= a[i] or a[i+1] > 2 * a[i]:
            print("NO")
            return
            
            
    print("YES")
    print(*a)

solve()