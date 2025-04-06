def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    remaining = n - sum(a)

    for i in range(k):
        a[i] += remaining // k
    
    remaining %= k

    for i in range(k - 1, k - 1 - remaining, -1):
        a[i] += 1
    
    valid = True
    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            valid = False
            break
    
    if valid:
        print("YES")
        print(*a)
    else:
        
        
        a = [i + 1 for i in range(k)]
        remaining = n - sum(a)

        if k > 1:
            
            
            low = 1
            high = 10**9
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                
                temp_a = [mid + i for i in range(k)]
                
                
                if sum(temp_a) <= n:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            if ans != -1:
                
                a = [ans + i for i in range(k)]
                rem = n - sum(a)
                
                for i in range(k - 1, k - 1 - rem, -1):
                    a[i] += 1
                
                v = True
                for i in range(k - 1):
                    if not (a[i] < a[i+1] <= 2 * a[i]):
                        v = False
                        break
                
                
                if v:
                    print("YES")
                    print(*a)
                    return
        
        
        print("NO")

solve()