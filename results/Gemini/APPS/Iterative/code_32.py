def solve():
    n = int(input())
    
    curr_pos = 0  # 0 is North Pole, 20000 is South Pole
    
    for _ in range(n):
        t, direction = input().split()
        t = int(t)
        
        if curr_pos == 0 and direction != "South":
            print("NO")
            return
        
        if curr_pos == 20000 and direction != "North":
            print("NO")
            return
        
        if direction == "North":
            curr_pos -= t
            if curr_pos < 0:
                print("NO")
                return
        elif direction == "South":
            curr_pos += t
            if curr_pos > 20000:
                print("NO")
                return
        # West and East do not change the position between the North and South poles
        

    if curr_pos == 0:
        print("YES")
    else:
        print("NO")

solve()