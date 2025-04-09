def solve():
    n = int(input())
    
    if n == 0:
        print(0, 0)
        return
    
    layer = 0
    count = 0
    while True:
        if count + 6 * layer < n:
            count += 6 * layer
            layer += 1
        else:
            break
    
    rem = n - count
    
    if rem <= layer:
        x = 2 * layer - rem
        y = 2 * rem
    elif rem <= 2 * layer:
        x = layer - 2 * (rem - layer)
        y = 2 * layer
    elif rem <= 3 * layer:
        x = -layer - (rem - 2 * layer)
        y = 2 * layer - 2 * (rem - 2 * layer)
    elif rem <= 4 * layer:
        x = -2 * layer + (rem - 3 * layer)
        y = -2 * (rem - 3 * layer)
    elif rem <= 5 * layer:
        x = -layer + 2 * (rem - 4 * layer)
        y = -2 * layer
    else:
        x = layer + (rem - 5 * layer)
        y = -2 * layer + 2 * (rem - 5 * layer)
        
    print(x, y)

solve()