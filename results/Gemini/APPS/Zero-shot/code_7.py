n, m = map(int, input().split())

low = 0
high = 2 * 10**9

ans = high

while low <= high:
    mid = (low + high) // 2
    
    total_sparrows = mid * (mid + 1) // 2
    
    if n + mid * m >= total_sparrows:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)