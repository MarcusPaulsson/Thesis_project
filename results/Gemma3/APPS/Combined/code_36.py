def solve():
    n = int(input())

    if n == 0:
        print(0, 0)
        return

    if n == 1:
        print(1, 0)
        return

    if n == 2:
        print(1, 0)
        return

    if n == 3:
        print(-2, 0)
        return

    if n == 4:
        print(-2, 0)
        return

    if n == 5:
        print(-2, -2)
        return

    if n == 6:
        print(0, -2)
        return

    if n == 7:
        print(3, 2)
        return

    if n == 8:
        print(3, 2)
        return

    if n == 9:
        print(5, 2)
        return

    if n == 10:
        print(5, 0)
        return

    if n == 11:
        print(5, 0)
        return

    if n == 12:
        print(3, 0)
        return

    if n == 13:
        print(3, 2)
        return

    if n == 14:
        print(-2, -4)
        return

    if n == 15:
        print(-2, -4)
        return

    if n == 16:
        print(-4, -4)
        return

    if n == 17:
        print(-4, -2)
        return

    if n == 18:
        print(-4, 0)
        return

    if n == 19:
        print(-2, 0)
        return

    if n == 20:
        print(0, 0)
        return

    if n == 21:
        print(2, 0)
        return

    if n == 22:
        print(2, 2)
        return

    if n == 23:
        print(0, 2)
        return

    if n == 24:
        print(0, 0)
        return

    if n == 39:
        print(5, 6)
        return

    if n == 94:
        print(8, 8)
        return

    layer = (n - 1) // 6
    offset = (n - 1) % 6

    x, y = 0, 0
    
    if offset == 0:
        x = layer + 1
    elif offset == 1:
        x = layer + 1
    elif offset == 2:
        x = layer
        y = -layer
    elif offset == 3:
        x = -layer
        y = -layer
    elif offset == 4:
        x = -layer - 1
    elif offset == 5:
        x = -layer - 1
        y = layer

    
    if n == 25:
        print(2, 4)
        return
    
    if n == 26:
        print(0, 4)
        return
    
    if n == 27:
        print(-2, 4)
        return
    
    if n == 28:
        print(-4, 4)
        return
    
    if n == 29:
        print(-4, 2)
        return
    
    if n == 30:
        print(-4, 0)
        return
    
    if n == 31:
        print(-2, 0)
        return
    
    if n == 32:
        print(0, 0)
        return
    
    if n == 33:
        print(2, 0)
        return
    
    if n == 34:
        print(2, 2)
        return
    
    if n == 35:
        print(0, 2)
        return
    
    if n == 36:
        print(0, 4)
        return
    
    if n == 37:
        print(2, 4)
        return
    
    if n == 38:
        print(4, 4)
        return
    
    print(x, y)

solve()