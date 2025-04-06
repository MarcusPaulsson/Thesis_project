def solve():
    n = int(input())
    
    if n == 0:
        print(0, 0)
        return
    
    l, r = 0, 10**9
    k = 0
    while l <= r:
        mid = (l + r) // 2
        if 3 * mid * (mid + 1) >= n:
            k = mid
            r = mid - 1
        else:
            l = mid + 1
            
    moves_in_prev_layers = 3 * (k - 1) * k if k > 0 else 0
    remaining_moves = n - moves_in_prev_layers
    
    x, y = 2 * k, 0
    
    if remaining_moves <= k:
        x -= 2 * (remaining_moves)
    elif remaining_moves <= 2 * k:
        x -= 2 * k
        remaining_moves -= k
        x += remaining_moves * (-1)
        y += remaining_moves * 2
        
    elif remaining_moves <= 3 * k:
        x -= k
        y += 2 * k
        remaining_moves -= 2 * k
        x += remaining_moves * (-1)
        
    elif remaining_moves <= 4 * k:
        x -= remaining_moves - 3 * k
        y -= 2 * (remaining_moves - 3 * k)
        x += k
        y += 2 * k
        remaining_moves -= 3 * k

    elif remaining_moves <= 5 * k:
        x += k
        y -= 2*k
        remaining_moves -= 4*k
        x += remaining_moves
        
    else:
        x += 2*k
        remaining_moves -= 5*k
        x += remaining_moves
        y += remaining_moves * (-2)
        y -= 2*k
        

    print(x, y)

solve()