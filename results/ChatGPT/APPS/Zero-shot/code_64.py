def time_to_meet(t, test_cases):
    results = []
    for i in range(t):
        n, l = test_cases[i][0]
        flags = test_cases[i][1]
        
        # Initial speeds
        speed1 = 1.0  # Speed of car 1
        speed2 = 1.0  # Speed of car 2
        pos1 = 0.0    # Position of car 1
        pos2 = l      # Position of car 2
        
        time = 0.0
        
        # Process each flag and calculate the meeting time
        for flag in flags:
            # Time for car 1 to reach the next flag
            time_to_flag1 = (flag - pos1) / speed1
            # Time for car 2 to reach the next flag
            time_to_flag2 = (pos2 - flag) / speed2
            
            if time_to_flag1 < time_to_flag2:
                # Car 1 reaches the flag first
                time += time_to_flag1
                pos1 = flag
                speed1 += 1.0
                # Update position of car 2
                pos2 -= speed2 * time_to_flag1
                # Increment car 2 speed as it moves
                time_to_flag2 -= time_to_flag1
                time_to_flag2 += (pos2 - pos1) / (speed1 + speed2)
                time += time_to_flag2
                break
            else:
                # Car 2 reaches the flag first
                time += time_to_flag2
                pos2 = flag
                speed2 += 1.0
                # Update position of car 1
                pos1 += speed1 * time_to_flag2
                # Increment car 1 speed as it moves
                time_to_flag1 -= time_to_flag2
                time_to_flag1 += (pos2 - pos1) / (speed1 + speed2)
                time += time_to_flag1
                break
        else:
            # If we finished all flags and haven't met yet
            time += (pos2 - pos1) / (speed1 + speed2)
        
        results.append(f"{time:.12f}")
    
    return results

# Example input processing
import sys

input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
test_cases = []

line_index = 1
for _ in range(t):
    n, l = map(int, data[line_index].split())
    flags = list(map(int, data[line_index + 1].split()))
    test_cases.append(((n, l), flags))
    line_index += 2

results = time_to_meet(t, test_cases)
print("\n".join(results))