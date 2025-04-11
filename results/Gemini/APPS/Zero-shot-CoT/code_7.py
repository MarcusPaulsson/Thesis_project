n, m = map(int, input().split())

left = 0
right = 2 * 10**9

while left <= right:
    mid = (left + right) // 2
    
    total_sparrows = (mid * (mid + 1)) // 2
    
    if total_sparrows >= n + mid * m:
        right = mid - 1
    else:
        left = mid + 1

print(left)