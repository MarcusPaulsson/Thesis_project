def solve():
    n, m = map(int, input().split())
    field = [input() for _ in range(n)]
    
    if n % 3 != 0:
        print("NO")
        return
    
    stripe_height = n // 3
    
    colors = set()
    
    for i in range(stripe_height):
        color = field[i][0]
        for j in range(m):
            if field[i][j] != color:
                print("NO")
                return
        colors.add(color)
        
    for i in range(stripe_height, 2 * stripe_height):
        color = field[i][0]
        for j in range(m):
            if field[i][j] != color:
                print("NO")
                return
        colors.add(color)
        
    for i in range(2 * stripe_height, n):
        color = field[i][0]
        for j in range(m):
            if field[i][j] != color:
                print("NO")
                return
        colors.add(color)
        
    if len(colors) != 3:
        print("NO")
        return
    
    print("YES")

solve()