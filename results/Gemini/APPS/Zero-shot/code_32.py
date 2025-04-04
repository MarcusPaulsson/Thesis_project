def solve():
    n = int(input())
    
    current_pos = 0  # 0 is north pole, 20000 is south pole
    
    for _ in range(n):
        t, direction = input().split()
        t = int(t)
        
        if current_pos == 0:
            if direction != "South":
                print("NO")
                return
            current_pos += t
        elif current_pos == 20000:
            if direction != "North":
                print("NO")
                return
            current_pos -= t
        else:
            if direction == "North":
                current_pos -= t
            elif direction == "South":
                current_pos += t
            else:
                pass # West or East, doesn't change north-south position
        
        if current_pos < 0 or current_pos > 20000:
            print("NO")
            return
    
    if current_pos == 0:
        print("YES")
    else:
        print("NO")

solve()