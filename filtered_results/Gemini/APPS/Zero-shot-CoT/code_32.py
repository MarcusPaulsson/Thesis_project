def solve():
    n = int(input())
    
    current_pos = 0  # 0 is North Pole, 20000 is South Pole
    
    for _ in range(n):
        t, direction = input().split()
        t = int(t)
        
        if current_pos == 0:
            if direction != "South":
                print("NO")
                return
            current_pos += t
            if current_pos > 20000:
                print("NO")
                return
        elif current_pos == 20000:
            if direction != "North":
                print("NO")
                return
            current_pos -= t
            if current_pos < 0:
                print("NO")
                return
        else:
            if direction == "North":
                current_pos -= t
                if current_pos < 0:
                    print("NO")
                    return
            elif direction == "South":
                current_pos += t
                if current_pos > 20000:
                    print("NO")
                    return
            else:
                pass 
                
    if current_pos == 0:
        print("YES")
    else:
        print("NO")

solve()