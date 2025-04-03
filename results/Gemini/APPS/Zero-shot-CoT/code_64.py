def solve():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    pos1 = 0
    pos2 = l
    speed1 = 1
    speed2 = 1
    time = 0

    i = 0
    j = n - 1

    while True:
        time1 = float('inf')
        time2 = float('inf')

        if i <= n - 1:
            time1 = (a[i] - pos1) / speed1
        else:
            time1 = (pos2 - pos1) / (speed1 + speed2)
            
        if j >= 0:
            time2 = (pos2 - a[j]) / speed2
        else:
            time2 = (pos2 - pos1) / (speed1 + speed2)
        
        if time1 < time2:
            time += time1
            pos1 += time1 * speed1
            pos2 -= time1 * speed2
            speed1 += 1
            i += 1
        elif time2 < time1:
            time += time2
            pos1 += time2 * speed1
            pos2 -= time2 * speed2
            speed2 += 1
            j -= 1
        else:
            if i <= n - 1 and j >= 0:
                time += time1
                pos1 += time1 * speed1
                pos2 -= time1 * speed2
                speed1 += 1
                speed2 += 1
                i += 1
                j -= 1
            else:
                time += (pos2 - pos1) / (speed1 + speed2)
                break
        
        if i > n - 1 and j < 0:
            break
        
        if pos1 >= pos2:
            break

    print(time)


t = int(input())
for _ in range(t):
    solve()