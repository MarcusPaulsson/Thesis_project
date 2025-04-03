def solve():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    def calculate_time(time):
        pos1 = 0
        speed1 = 1
        idx1 = 0
        time1 = 0
        
        while time1 < time:
            if idx1 < n:
                dist_to_flag = a[idx1] - pos1
                time_to_flag = dist_to_flag / speed1
                
                if time1 + time_to_flag <= time:
                    time1 += time_to_flag
                    pos1 = a[idx1]
                    speed1 += 1
                    idx1 += 1
                else:
                    pos1 += speed1 * (time - time1)
                    time1 = time
            else:
                pos1 += speed1 * (time - time1)
                time1 = time

        pos2 = l
        speed2 = 1
        idx2 = n - 1
        time2 = 0
        
        while time2 < time:
            if idx2 >= 0:
                dist_to_flag = pos2 - a[idx2]
                time_to_flag = dist_to_flag / speed2
                
                if time2 + time_to_flag <= time:
                    time2 += time_to_flag
                    pos2 = a[idx2]
                    speed2 += 1
                    idx2 -= 1
                else:
                    pos2 -= speed2 * (time - time2)
                    time2 = time
            else:
                pos2 -= speed2 * (time - time2)
                time2 = time
        
        return pos1, pos2
    
    low = 0
    high = l
    
    for _ in range(100):
        mid = (low + high) / 2
        pos1, pos2 = calculate_time(mid)
        
        if pos1 < pos2:
            low = mid
        else:
            high = mid
            
    print(f"{low:.12f}")

t = int(input())
for _ in range(t):
    solve()