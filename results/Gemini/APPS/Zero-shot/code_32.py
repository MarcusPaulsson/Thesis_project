def solve():
    n = int(input())
    
    current_pos = 0  # Distance from North Pole (0 to 20000)
    
    for _ in range(n):
        t, direction = input().split()
        t = int(t)
        
        if current_pos == 0:
            if direction != "South":
                print("NO")
                return
            else:
                current_pos += t
        elif current_pos == 20000:
            if direction != "North":
                print("NO")
                return
            else:
                current_pos -= t
        else:
            if direction == "South":
                current_pos += t
            elif direction == "North":
                current_pos -= t
            
            if current_pos < 0 or current_pos > 20000:
                print("NO")
                return
    
    if current_pos == 0:
        print("YES")
    else:
        print("NO")

solve()