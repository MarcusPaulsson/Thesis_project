def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    count = 0
    left = 0
    right = n - 1
    
    while left <= right:
        if a[left] <= k:
            count += 1
            left += 1
        elif a[right] <= k:
            count += 1
            right -= 1
        else:
            break
            
    print(count)

solve()