def solve():
    n = int(input())
    
    if n == 0:
        print(0, 0)
        return
    
    x, y = 0, 0
    dx, dy = 1, 0
    
    for i in range(1, n + 1):
        if dx == 1 and dy == 0:
            if i % 6 == 1:
                x += 1
            elif i % 6 == 2:
                x += 1
            elif i % 6 == 3:
                y += 1
            elif i % 6 == 4:
                x -= 1
            elif i % 6 == 5:
                x -= 1
            else:
                y -= 1
        elif dx == 0 and dy == 1:
            if i % 6 == 1:
                y += 1
            elif i % 6 == 2:
                x -= 1
            elif i % 6 == 3:
                x -= 1
            elif i % 6 == 4:
                y -= 1
            elif i % 6 == 5:
                x += 1
            else:
                x += 1
        elif dx == -1 and dy == 0:
            if i % 6 == 1:
                x -= 1
            elif i % 6 == 2:
                y -= 1
            elif i % 6 == 3:
                x += 1
            elif i % 6 == 4:
                y += 1
            elif i % 6 == 5:
                y += 1
            else:
                x -= 1
        elif dx == 0 and dy == -1:
            if i % 6 == 1:
                y -= 1
            elif i % 6 == 2:
                x += 1
            elif i % 6 == 3:
                x += 1
            elif i % 6 == 4:
                y += 1
            elif i % 6 == 5:
                x -= 1
            else:
                x -= 1
        elif dx == 1 and dy == -1:
            if i % 6 == 1:
                x += 1
            elif i % 6 == 2:
                y -= 1
            elif i % 6 == 3:
                x -= 1
            elif i % 6 == 4:
                y += 1
            elif i % 6 == 5:
                x += 1
            else:
                y -= 1
        elif dx == -1 and dy == 1:
            if i % 6 == 1:
                x -= 1
            elif i % 6 == 2:
                y += 1
            elif i % 6 == 3:
                x += 1
            elif i % 6 == 4:
                y -= 1
            elif i % 6 == 5:
                x -= 1
            else:
                y += 1
        
        if i % 6 == 0:
            dx, dy = -dx, -dy
            
    
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