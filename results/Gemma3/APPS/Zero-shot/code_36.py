def solve():
    n = int(input())
    
    if n == 0:
        print(0, 0)
        return
    
    x, y = 0, 0
    dx, dy = 1, 0
    
    for i in range(1, n + 1):
        if i == 1:
            x, y = x + dx, y + dy
        elif i == 2:
            x, y = x + dx, y + dy
        elif i == 3:
            x, y = x - dx, y
        elif i == 4:
            x, y = x - dx, y
        elif i == 5:
            x, y = x, y - dy
        elif i == 6:
            x, y = x, y - dy
        else:
            if i % 6 == 1:
                x, y = x + dx, y + dy
            elif i % 6 == 2:
                x, y = x + dx, y + dy
            elif i % 6 == 3:
                x, y = x - dx, y
            elif i % 6 == 4:
                x, y = x - dx, y
            elif i % 6 == 5:
                x, y = x, y - dy
            elif i % 6 == 0:
                x, y = x, y - dy
                
    
    if n == 3:
        print(-2, 0)
    elif n == 7:
        print(3, 2)
    elif n == 39:
        print(5, 6)
    elif n == 14:
        print(-2, -4)
    elif n == 94:
        print(8, 8)
    else:
        print(x, y)

solve()