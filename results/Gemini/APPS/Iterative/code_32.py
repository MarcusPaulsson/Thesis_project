def solve():
    n = int(input())
    
    distance = 0
    
    for _ in range(n):
        t, direction = input().split()
        t = int(t)
        
        if distance == 0 and direction != "South":
            print("NO")
            return
        
        if distance == 20000 and direction != "North":
            print("NO")
            return
            
        if direction == "South":
            distance += t
        elif direction == "North":
            distance -= t
        elif direction == "West" or direction == "East":
            pass
        
        if distance < 0 or distance > 20000:
            print("NO")
            return
    
    if distance == 0:
        print("YES")
    else:
        print("NO")

solve()