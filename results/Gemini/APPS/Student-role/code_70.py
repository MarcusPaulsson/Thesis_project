def solve():
    time1 = input()
    time2 = input()
    
    h1 = int(time1[:2])
    m1 = int(time1[3:])
    h2 = int(time2[:2])
    m2 = int(time2[3:])
    
    start_minutes = h1 * 60 + m1
    end_minutes = h2 * 60 + m2
    
    mid_minutes = (start_minutes + end_minutes) // 2
    
    h3 = mid_minutes // 60
    m3 = mid_minutes % 60
    
    print(f"{h3:02}:{m3:02}")

solve()