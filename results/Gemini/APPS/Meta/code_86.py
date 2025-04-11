def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [i + 1 for i in range(k)]
    diff = n - sum(a)

    for i in range(k):
        a[i] += diff // k
    
    diff %= k
    
    for i in range(k - 1, k - 1 - diff, -1):
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
        
        a = [0] * k
        
        low = 1
        high = n
        
        best_a = None
        
        while low <= high:
            mid = (low + high) // 2
            
            a[0] = mid
            
            possible = True
            
            for i in range(1, k):
                a[i] = a[i-1] + 1
            
            current_sum = sum(a)
            
            if current_sum > n:
                high = mid - 1
                continue
            
            diff = n - current_sum
            
            for i in range(k):
                a[i] += diff // k
            
            diff %= k
            
            for i in range(k - 1, k - 1 - diff, -1):
                a[i] += 1
            
            
            valid = True
            for i in range(k - 1):
                if not (a[i] < a[i+1] <= 2 * a[i]):
                    valid = False
                    break
            
            if valid:
                best_a = a
                high = mid - 1
            else:
                low = mid + 1
        
        if best_a is not None:
            print("YES")
            print(*best_a)
        else:
            print("NO")

solve()