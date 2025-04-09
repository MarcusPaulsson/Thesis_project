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
    
    n -= 3 * k * (k - 1)
    
    x, y = 2 * k, 0
    
    if n <= k:
        x -= 2 * (n)
        y += 2 * n
    elif n <= 2 * k:
        x -= 2 * k
        y += 2 * k
        n -= k
        x += (-n * 2 + n * 2)
        y += (-n) * 2
        
        
        x += (-(n))
        y += (-n) * 2
        
        x = x + 2*(2*k - n)
        
        x = x - (n - k)
        y = y + (n - k)*2
        
        x = 2*k - 2*(n - k)
        y = -2*(n-k)
        x, y = -2*k + 2*(n-k), 2*(n-k)
        
        x, y = x - (n-k)*2, y
        
        x, y = x - (n-k)*2, y
        
        x, y = 2*k - (n-k)*2, 0 + (n-k)*2
    elif n <= 3 * k:
        x -= 2 * k
        y += 2 * k
        n -= 2 * k

        x -= k
    elif n <= 4 * k:
        x -= 2 * k
        y += 2 * k
        n -= 2 * k
        
        x -= k
        
    elif n <= 5 * k:
        x -= 2 * k
        y += 2 * k
        n -= 2 * k
        
        x -= k
        
    else:
        x -= 2 * k
        y += 2 * k
        n -= 2 * k
        
        x -= k
        
    
    
    x, y = 2 * k, 0
    
    if n <= k:
        x -= n * 2
        y += n * 2
    elif n <= 2 * k:
        n -= k
        x -= k * 2
        y += k * 2
        x += (-(n))
        y += (-n) * 2
    elif n <= 3 * k:
        n -= 2 * k
        x -= k * 2
        y += k * 2
        x -= k
        y -= (n*2)
        
        x -= (n*2)
    elif n <= 4 * k:
        n -= 3 * k
        x -= k * 2
        y += k * 2
        x -= k
        y -= k*2
        x += n * 2
        
        
    elif n <= 5 * k:
        n -= 4*k
        x -= k * 2
        y += k * 2
        x -= k
        y -= k*2
        x += k * 2
        x += n * 2
        y += n * 2
        
    else:
        n -= 5 * k
        x -= k * 2
        y += k * 2
        x -= k
        y -= k*2
        x += k * 2
        x += k * 2
        y += k * 2
        
        
        x -= n*2
        
    x, y = 2 * k, 0
    
    if n <= k:
        x -= 2 * n
        y += 2 * n
    elif n <= 2 * k:
        x -= 2 * k
        y += 2 * k
        n -= k
        x -= n
        y -= n * 2
        x = x
    elif n <= 3 * k:
        x -= 2 * k
        y += 2 * k
        n -= 2 * k
        x +=(n)
        y -= (n) * 2
        
        x = x
    elif n <= 4 * k:
        x -= 2 * k
        y += 2 * k
        n -= 3 * k
        x += 2*k
        y += 0
        x +=n*2
        y +=0
    elif n <= 5 * k:
        x -= 2 * k
        y += 2 * k
        n -= 4 * k
        x += k
        y -= k * 2
        x += n * 2
        y += n * 2
        
    else:
        x -= 2 * k
        y += 2 * k
        n -= 5 * k
        x += k
        y -= k * 2
    
    x, y = 2 * k, 0
    
    dx = 0
    dy = 0

    if n <= k:
        dx = -2
        dy = 2
        x += dx * n
        y += dy * n
    elif n <= 2 * k:
        dx = -1
        dy = -2
        x += -2*k
        y += 2*k
        n -= k
        x += dx * n
        y += dy * n
    elif n <= 3 * k:
        dx = 1
        dy = -2
        x += -2*k
        y += 2*k
        n -= 2 * k
        x += -k
        y -= k*2
        x += dx * n
        y += dy * n
    elif n <= 4 * k:
        dx = 2
        dy = 0
        x += -2*k
        y += 2*k
        n -= 3 * k
        x += -k
        y -= k*2
        x += n * dx
        y += n * dy
    elif n <= 5 * k:
        dx = 1
        dy = 2
        x += -2*k
        y += 2*k
        n -= 4 * k
        x += -k
        y -= k*2
        x += 2*k
        x += n*dx
        y += n*dy

    else:
        dx = -1
        dy = 2
        x += -2*k
        y += 2*k
        n -= 5 * k
        x += -k
        y -= k*2
        x += 2*k
        x += n * dx
        y += n * dy
        
        
    x, y = 2 * k, 0
    
    if n <= k:
        x -= 2*n
        y += 2*n
    elif n <= 2*k:
        x -= 2*k
        y += 2*k
        n -= k
        x -= n
        y -= 2*n
    elif n <= 3*k:
        x -= 2*k
        y += 2*k
        n -= 2*k
        x += n
        y -= 2*n
    elif n <= 4*k:
        x -= 2*k
        y += 2*k
        n -= 3*k
        x += 2*n
    elif n <= 5*k:
        x -= 2*k
        y += 2*k
        n -= 4*k
        x += n
        y += 2*n
    else:
        x -= 2*k
        y += 2*k
        n -= 5*k
        x -= n
        y += 2*n
        
    x, y = 2 * k, 0
    
    if n <= k:
        x -= 2 * n
        y += 2 * n
    elif n <= 2 * k:
        x -= 2 * k
        y += 2 * k
        n -= k
        x -= n
        y -= 2 * n
    elif n <= 3 * k:
        x -= 2 * k
        y += 2 * k
        n -= 2 * k
        x += n
        y -= 2 * n
    elif n <= 4 * k:
        x -= 2 * k
        y += 2 * k
        n -= 3 * k
        x += 2 * n
    elif n <= 5 * k:
        x -= 2 * k
        y += 2 * k
        n -= 4 * k
        x += n
        y += 2 * n
    else:
        x -= 2 * k
        y += 2 * k
        n -= 5 * k
        x -= n
        y += 2 * n

    x, y = 2*k, 0
    
    if n <= k:
        x -= 2*n
        y += 2*n
    elif n <= 2*k:
        x -= 2*k
        y += 2*k
        n -= k
        x -= n
        y -= 2*n
    elif n <= 3*k:
        x -= 2*k
        y += 2*k
        n -= 2*k
        x += n
        y -= 2*n
    elif n <= 4*k:
        x -= 2*k
        y += 2*k
        n -= 3*k
        x += 2*n
    elif n <= 5*k:
        x -= 2*k
        y += 2*k
        n -= 4*k
        x += n
        y += 2*n
    else:
        x -= 2*k
        y += 2*k
        n -= 5*k
        x -= n
        y += 2*n
    

    print(x, y)
solve()