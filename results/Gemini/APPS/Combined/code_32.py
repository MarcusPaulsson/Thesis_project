def solve():
    n = int(input())
    position = 0 
    
    for _ in range(n):
        t, direction = input().split()
        t = int(t)
        
        if position == 0:
            if direction != "South":
                print("NO")
                return
            position += t
        elif position == 20000:
            if direction != "North":
                print("NO")
                return
            position -= t
        else:
            if direction == "South":
                position += t
            elif direction == "North":
                position -= t
            
        if position < 0 or position > 20000:
            print("NO")
            return
    
    if position == 0:
        print("YES")
    else:
        print("NO")

solve()