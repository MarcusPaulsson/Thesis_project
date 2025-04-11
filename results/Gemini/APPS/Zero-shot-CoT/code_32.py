def solve():
    n = int(input())
    
    current_pos = 0 
    
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
            current_pos -= t
            if current_pos < 0:
                current_pos = 0
        elif direction == "South":
            current_pos += t
            if current_pos > 20000:
                current_pos = 20000
                
    if current_pos == 0:
        print("YES")
    else:
        print("NO")

solve()