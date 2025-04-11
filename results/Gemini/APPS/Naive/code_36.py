def solve():
    n = int(input())
    
    if n == 0:
        print(0, 0)
        return
    
    layer = 0
    count = 0
    while True:
        if count + 6 * layer <= n:
            count += 6 * layer
            layer += 1
        else:
            break
    
    remaining = n - count
    
    x, y = 2 * (layer - 1), 0
    
    if remaining == 0:
        print(x, y)
        return
    
    if remaining <= layer:
        x -= 2 * remaining
        print(x, y)
        return
    
    remaining -= layer
    x -= 2 * layer
    y += 2 * remaining
    
    if remaining <= layer:
        print(x, y)
        return
    
    remaining -= layer
    x += remaining * 2
    y += remaining * 2
    
    if remaining <= layer:
        print(x, y)
        return
    
    remaining -= layer
    x += 2 * remaining
    
    y -= 2 * remaining
    
    if remaining <= layer:
        print(x, y)
        return
    
    remaining -= layer
    x -= 2 * remaining
    y -= 2 * remaining
    
    if remaining <= layer:
        print(x, y)
        return
    
    remaining -= layer
    x -= 2 * remaining
    
    print(x, y)

solve()