def solve():
    n = int(input())
    
    if n == 0:
        print(0, 0)
        return
    
    l, r = 1, 10**9
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
        y += 2 * (n)
    elif n <= 2 * k:
        x -= 2 * k
        y += 2 * k
        n -= k
        x += (-n * 2 + n * 2)
        y += (-n * 2)
        x += (n)
        y += (-n * 2)

        x += (n * 2 - n * 2)
        y += (-n * 2)
        x += (n)
        y += (-n * 2)
        x += 2*(-n)
    elif n <= 3 * k:
        x -= 2 * k
        y += 2 * k
        n -= k
        x += (-k)
        y += (-2*k)
        n -= k
        x -= k*2
    elif n <= 4 * k:
        x -= 4 * k
        y -= 2 * k
        n -= 3 * k
        x += (-n*2)
    elif n <= 5 * k:
        x -= 4 * k
        y -= 2 * k
        n -= 3 * k
        x += (-k*2)
        n -= k
        x += k*2
        y += k*2
        n -= k
        x += k*2
        y += k*2
        x += n*2
        y += n*2
    elif n <= 6 * k:
        x -= 4 * k
        y -= 2 * k
        n -= 3 * k
        x += (-k*2)
        n -= k
        x += k*2
        y += k*2
        n -= k
        x += k*2
        y += k*2
        n -= k
        x += k*2
        y += k*2
        n -= k
        x += k*2
        y += k*2
        x += k*2
        y += k*2
        x += n*2
        y += n*2
    else:
        pass
        
    n = int(n)
    x, y = 2 * k, 0
    
    if 1 <= n <= k:
        x -= n * 2
        y += n * 2
    elif k + 1 <= n <= 2 * k:
        x -= 2 * k
        y += 2 * k
        n -= k
        x += n
        y -= 2 * n
    elif 2 * k + 1 <= n <= 3 * k:
        x -= k
        y -= 2 * k
        n -= 2 * k
        x += n * -2
    elif 3 * k + 1 <= n <= 4 * k:
        x -= 3 * k
        y -= 2 * k
        n -= 3 * k
        x += n * -2
    elif 4 * k + 1 <= n <= 5 * k:
        x -= 5 * k
        y -= 2 * k
        n -= 4 * k
        x += n
        y += 2 * n
    else:
        x -= 4 * k
        y += 0
        n -= 3 * k
        x = -4*k
        y = -2*k
        n = int(n)
        if 1 <= n <= k:
            x -= n*2
        elif k + 1 <= n <= 2*k:
            x -= 2*k
            n -= k
            x += (n)
            y += (-2*n)
        elif 2*k + 1 <= n <= 3*k:
            x -= k
            y -= 2*k
            n -= 2*k
            x += (-2*n)
        elif 3*k + 1 <= n <= 4*k:
            x -= 3*k
            y -= 2*k
            n -= 3*k
            x += (-2*n)
        elif 4*k + 1 <= n <= 5*k:
            x -= 5*k
            y -= 2*k
            n -= 4*k
            x += (n)
            y += (2*n)
        elif 5*k + 1 <= n <= 6*k:
            x -= 4*k
            y += 0
            n -= 3*k
            x -= k*2
            n -= k
            x += (n)
            y += (2*n)

    x, y = 2 * k, 0
    
    if 1 <= n <= k:
      x -= 2 * n
      y += 2 * n
    elif k + 1 <= n <= 2 * k:
      x -= 2 * k
      y += 2 * k
      n -= k
      x += n
      y -= 2 * n
    elif 2 * k + 1 <= n <= 3 * k:
      x -= k
      y -= 2 * k
      n -= 2 * k
      x -= 2 * n
    elif 3 * k + 1 <= n <= 4 * k:
      x -= 3 * k
      y -= 2 * k
      n -= 3 * k
      x -= 2 * n
    elif 4 * k + 1 <= n <= 5 * k:
      x -= 5 * k
      y -= 2 * k
      n -= 4 * k
      x += n
      y += 2 * n
    else:
      x -= 4 * k
      y += 0
      n -= 3 * k
      x += k
      y -= 2 * k
      n -= 4 * k
      x -= 2 * k
      
    n = int(n)
    x, y = 2 * k, 0
    
    if 1 <= n <= k:
        x -= 2 * n
        y += 2 * n
    elif k + 1 <= n <= 2 * k:
        x -= 2 * k
        y += 2 * k
        n -= k
        x += n
        y -= 2 * n
    elif 2 * k + 1 <= n <= 3 * k:
        x -= k
        y -= 2 * k
        n -= 2 * k
        x -= 2 * n
    elif 3 * k + 1 <= n <= 4 * k:
        x -= 3 * k
        y -= 2 * k
        n -= 3 * k
        x -= 2 * n
    elif 4 * k + 1 <= n <= 5 * k:
        x -= 5 * k
        y -= 2 * k
        n -= 4 * k
        x += n
        y += 2 * n
    elif 5 * k + 1 <= n <= 6 * k:
        x -= 4 * k
        y += 0
        n -= 3 * k
        x = -4*k
        y = -2*k
        n = int(n)
        x -= k*2
        n -= k
        x += (n)
        y += (2*n)
    else:
        pass
    
    
    l, r = 1, 10**9
    k = 0
    while l <= r:
        mid = (l + r) // 2
        if (3 * mid * (mid + 1)) >= n:
            k = mid
            r = mid - 1
        else:
            l = mid + 1
            
    n -= 3 * k * (k - 1)
    x, y = 2 * k, 0
    
    if 1 <= n <= k:
        x -= 2 * n
        y += 2 * n
    elif k + 1 <= n <= 2 * k:
        x -= 2 * k
        y += 2 * k
        n -= k
        x += n
        y -= 2 * n
    elif 2 * k + 1 <= n <= 3 * k:
        x -= k
        y -= 2 * k
        n -= 2 * k
        x -= 2 * n
    elif 3 * k + 1 <= n <= 4 * k:
        x -= 3 * k
        y -= 2 * k
        n -= 3 * k
        x -= 2 * n
    elif 4 * k + 1 <= n <= 5 * k:
        x -= 5 * k
        y -= 2 * k
        n -= 4 * k
        x += n
        y += 2 * n
    elif 5 * k + 1 <= n <= 6 * k:
        x -= 4 * k
        y += 0
        n -= 3 * k
        x -= 2 * k
        n -= k
        x += n
        y += 2 * n
    else:
        pass
    
    print(x, y)
solve()