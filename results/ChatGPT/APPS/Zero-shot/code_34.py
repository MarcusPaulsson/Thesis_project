def max_min_pieces(n, a, b):
    left, right = 0, max(a, b)
    
    while left < right:
        mid = (left + right + 1) // 2
        if (a // mid) + (b // mid) >= n:
            left = mid
        else:
            right = mid - 1
            
    return left

n, a, b = map(int, input().split())
print(max_min_pieces(n, a, b))