def solve():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    flags1 = [0] + a
    flags2 = a + [l]

    pos1 = 0
    pos2 = l
    speed1 = 1
    speed2 = 1
    time = 0

    idx1 = 0
    idx2 = n

    while True:
        time_to_next_flag1 = float('inf')
        if idx1 <= n:
            time_to_next_flag1 = (flags1[idx1] - pos1) / speed1
        
        time_to_next_flag2 = float('inf')
        if idx2 >= 0:
            time_to_next_flag2 = (pos2 - flags2[idx2]) / speed2

        time_to_meet = (pos2 - pos1) / (speed1 + speed2)

        if time_to_meet <= time_to_next_flag1 and time_to_meet <= time_to_next_flag2:
            time += time_to_meet
            print(time)
            return
        elif time_to_next_flag1 <= time_to_next_flag2:
            time += time_to_next_flag1
            pos1 += time_to_next_flag1 * speed1
            pos2 -= time_to_next_flag1 * speed2
            speed1 += 1
            idx1 += 1
        else:
            time += time_to_next_flag2
            pos1 += time_to_next_flag2 * speed1
            pos2 -= time_to_next_flag2 * speed2
            speed2 += 1
            idx2 -= 1

t = int(input())
for _ in range(t):
    solve()