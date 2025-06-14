def solve():
    n = int(input())
    
    current_pos = 0  # 0 is North Pole, 20000 is South Pole
    
    for _ in range(n):
        t, direction = input().split()
        t = int(t)
        
        if current_pos == 0 and direction != "South":
            print("NO")
            return
        
        if current_pos == 20000 and direction != "North":
            print("NO")
            return
            
        if direction == "North":
            current_pos = max(0, current_pos - t)
        elif direction == "South":
            current_pos = min(20000, current_pos + t)
        # West and East directions do not affect the position
        
    if current_pos == 0:
        print("YES")
    else:
        print("NO")

solve()