def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [0] * k
    for i in range(k):
        a[i] = i + 1

    remaining = n - k * (k + 1) // 2

    for i in range(k):
        a[i] += remaining // k

    remaining %= k

    for i in range(k - 1, k - 1 - remaining, -1):
        a[i] += 1

    for i in range(k - 1):
        if a[i+1] > 2 * a[i]:
            diff = a[i+1] - 2 * a[i]
            a[i+1] -= diff
            a[k-1] += diff
            
    
    possible = True
    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2*a[i]):
            possible = False
            break
    
    if possible:
        print("YES")
        print(*a)
    else:
        
        a = [0] * k
        
        low = 1
        high = n
        
        best_a = None
        
        while low <= high:
            mid = (low + high) // 2
            
            temp_a = [0] * k
            temp_a[0] = mid
            
            possible = True
            total_sum = mid
            
            for i in range(1, k):
                next_val = temp_a[i-1] + 1
                
                if next_val > 2 * temp_a[i-1]:
                    possible = False
                    break
                    
                temp_a[i] = next_val
                total_sum += temp_a[i]
                
            if possible:
                if total_sum <= n:
                    remaining = n - total_sum
                    
                    for i in range(k):
                        temp_a[i] += remaining // k
                    remaining %= k
                    
                    for i in range(k -1, k - 1 - remaining, -1):
                        temp_a[i] += 1
                    
                    valid = True
                    for i in range(k - 1):
                        if not (temp_a[i] < temp_a[i+1] <= 2 * temp_a[i]):
                            valid = False
                            break
                    
                    if valid:
                        best_a = temp_a
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    high = mid - 1
            else:
                high = mid - 1
        
        if best_a is not None:
            print("YES")
            print(*best_a)
        else:
            print("NO")
            
solve()