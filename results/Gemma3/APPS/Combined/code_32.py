def solve():
    n = int(input())
    
    latitude = 20000
    longitude = 0
    
    for _ in range(n):
        t, direction = input().split()
        t = int(t)
        
        if latitude == 20000 and direction != "South":
            print("NO")
            return
        
        if latitude == -20000 and direction != "North":
            print("NO")
            return
        
        if direction == "North":
            latitude += t
        elif direction == "South":
            latitude -= t
        elif direction == "West":
            longitude -= t
        else:
            longitude += t
        
        latitude = max(-20000, min(latitude, 20000))
        longitude = longitude % 40000
        
    if latitude == 20000 and longitude == 0:
        print("YES")
    else:
        print("NO")

solve()