def solve():
    n = int(input())
    
    x = 20000  # North-South coordinate (positive North, negative South)
    y = 0  # East-West coordinate
    
    for _ in range(n):
        t, dir = input().split()
        t = int(t)
        
        if x == 20000 and dir == "North":
            print("NO")
            return
        if x == -20000 and dir == "South":
            print("NO")
            return
        
        if dir == "North":
            x += t
        elif dir == "South":
            x -= t
        elif dir == "East":
            y += t
        elif dir == "West":
            y -= t
        
        if x > 20000 or x < -20000:
            print("NO")
            return
        
        if x == 20000 and dir != "South":
            print("NO")
            return
        if x == -20000 and dir != "North":
            print("NO")
            return
            
    if x == 20000 and y == 0:
        print("YES")
    else:
        print("NO")

solve()