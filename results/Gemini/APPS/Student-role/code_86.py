def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("NO")
        return

    a = [0] * k
    remaining = n - k * (k + 1) // 2
    
    base = remaining // k
    rem = remaining % k
    
    for i in range(k):
        a[i] = i + 1 + base
        
    for i in range(k - 1, k - 1 - rem, -1):
        a[i] += 1

    
    for i in range(k - 1):
        if not (a[i] < a[i+1] <= 2 * a[i]):
            
            
            found = False
            for start in range(1, n + 1):
                temp_a = [0] * k
                temp_a[0] = start
                
                possible = True
                
                for i in range(1, k):
                    found_next = False
                    for next_val in range(temp_a[i-1] + 1, 2 * temp_a[i-1] + 1 + 1):
                        temp_a[i] = next_val
                        
                        
                        
                        
                        
                        found_next = True
                        break
                    if not found_next:
                        possible = False
                        break
                
                if possible and sum(temp_a) == n:
                    print("YES")
                    print(*temp_a)
                    return
            
            print("NO")
            return
    
    print("YES")
    print(*a)

solve()