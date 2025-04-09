def solve():
    n = int(input())
    
    x = 0.0
    y = 20000.0
    
    radius = 20000.0
    
    for _ in range(n):
        t, dir = input().split()
        t = float(t)
        
        if abs(y) < 1e-6 and abs(x) < 1e-6:
            if dir != "South":
                print("NO")
                return
        elif abs(y + 20000.0) < 1e-6 and abs(x) < 1e-6:
            if dir != "North":
                print("NO")
                return
        
        if dir == "North":
            y += t
        elif dir == "South":
            y -= t
        elif dir == "East":
            x += t
        elif dir == "West":
            x -= t
        
        if abs(x) > radius or abs(y) > radius:
            print("NO")
            return
        
        
    if abs(x) < 1e-6 and abs(y - 20000.0) < 1e-6:
        print("YES")
    else:
        print("NO")

solve()