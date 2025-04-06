def solve():
    n = int(input())
    
    if n == 0:
        print(0, 0)
        return
    
    l = 0
    while True:
        if 3 * l * (l + 1) >= n:
            break
        l += 1
    
    diff = n - 3 * l * (l - 1)
    
    if diff <= l:
        x = 2 * l - diff
        y = 2 * diff
    elif diff <= 2 * l:
        x = l - 2 * (diff - l)
        y = 2 * l
    elif diff <= 3 * l:
        x = -l - (diff - 2 * l)
        y = 2 * l - 2 * (diff - 2 * l)
    elif diff <= 4 * l:
        x = -2 * l + (diff - 3 * l)
        y = -2 * (diff - 3 * l)
    elif diff <= 5 * l:
        x = -l + 2 * (diff - 4 * l)
        y = -2 * l
    else:
        x = l + (diff - 5 * l)
        y = -2 * l + 2 * (diff - 5 * l)
    
    print(x, y)

solve()