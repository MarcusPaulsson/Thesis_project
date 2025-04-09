def solve():
    n = int(input())
    
    if n == 0:
        print(0, 0)
        return

    k = 0
    while True:
        if 3 * k * (k + 1) >= n:
            break
        k += 1

    moves_in_prev_layer = 3 * (k - 1) * k if k > 0 else 0
    rem = n - moves_in_prev_layer
    
    x = 2 * k
    y = 0

    if rem <= k:
        x -= 2 * rem
        print(x, y)
    elif rem <= 2 * k:
        x -= 2 * k
        rem -= k
        x += rem
        y += 2 * rem
        print(x, y)
    elif rem <= 3 * k:
        rem -= 2 * k
        x += k
        y += 2 * k
        x -= rem
        print(x, y)
    elif rem <= 4 * k:
        rem -= 3 * k
        x += k
        y += 2 * k
        x -= 2 * rem
        y -= rem * 2
        print(x, y)
    elif rem <= 5 * k:
        rem -= 4 * k
        x -= k 
        y -= 2 * k
        x -= rem
        y -= 2 * rem
        print(x, y)
    else:
        rem -= 5 * k
        x -= 2 * k
        y -= 0
        x += rem * 1
        y -= rem * 2
        print(x, y)

solve()