def time_to_meet(n, l, flags):
    # Initial positions and speeds
    car1_pos = 0
    car2_pos = l
    car1_speed = 1
    car2_speed = 1
    
    flags1 = flags.copy()  # For the first car
    flags2 = [l - a for a in reversed(flags)]  # Mirror positions for the second car

    # Initialize the time taken until the next flag
    time1 = 0
    time2 = 0

    while flags1 or flags2:
        if not flags1:
            # Only car2 is moving
            time_to_next_flag = (flags2[-1] - car2_pos) / car2_speed
            time2 += time_to_next_flag
            car2_pos = flags2.pop()
            car2_speed += 1
        elif not flags2:
            # Only car1 is moving
            time_to_next_flag = (flags1[0] - car1_pos) / car1_speed
            time1 += time_to_next_flag
            car1_pos = flags1.pop(0)
            car1_speed += 1
        else:
            # Both cars are moving towards their next flags
            time_to_next_flag1 = (flags1[0] - car1_pos) / car1_speed
            time_to_next_flag2 = (flags2[-1] - car2_pos) / car2_speed
            
            if time_to_next_flag1 < time_to_next_flag2:
                time1 += time_to_next_flag1
                car1_pos = flags1.pop(0)
                car1_speed += 1
                # Move car2 during the time taken by car1
                car2_pos += car2_speed * time_to_next_flag1
                if car1_pos >= car2_pos:  # They meet
                    return time1
            else:
                time2 += time_to_next_flag2
                car2_pos = flags2.pop()
                car2_speed += 1
                # Move car1 during the time taken by car2
                car1_pos += car1_speed * time_to_next_flag2
                if car1_pos >= car2_pos:  # They meet
                    return time2 + time1

    # Final meeting time calculation if we exhaust all flags
    if car1_pos < car2_pos:
        meeting_time = (car2_pos - car1_pos) / (car1_speed + car2_speed)
        return time1 + time2 + meeting_time
    return time1 + time2

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    output = []
    
    index = 1
    for _ in range(t):
        n, l = map(int, data[index].split())
        flags = list(map(int, data[index + 1].split()))
        index += 2
        
        result = time_to_meet(n, l, flags)
        output.append(f"{result:.12f}")
    
    print("\n".join(output))

if __name__ == "__main__":
    main()