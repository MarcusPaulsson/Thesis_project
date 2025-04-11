def max_min_pieces(n, a, b):
    low, high = 1, max(a, b)
    while low < high:
        mid = (low + high + 1) // 2
        if (a // mid) + (b // mid) >= n:
            low = mid
        else:
            high = mid - 1
    return low

n, a, b = map(int, input().split())
print(max_min_pieces(n, a, b))