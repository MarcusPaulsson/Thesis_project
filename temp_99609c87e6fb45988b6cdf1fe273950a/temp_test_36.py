n, k = map(int, input().split())

# Minimum problems needed to satisfy the conditions
min_needed = k * (k + 1) // 2  # 1 + 2 + ... + k
if n < min_needed:
    print("NO")
else:
    # Start with the minimum valid array
    a = [i for i in range(1, k + 1)]
    total = sum(a)
    
    # We need to add (n - total) to the last element
    additional = n - total
    a[-1] += additional
    
    # Check if we still satisfy the conditions
    if a[-1] <= 2 * a[-2]:
        print("YES")
        print(' '.join(map(str, a)))
    else:
        print("NO")