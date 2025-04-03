def time_to_meet(t, test_cases):
    results = []
    
    for case in test_cases:
        n, l, flags = case
        pos1 = 0  # position of the first car
        pos2 = l  # position of the second car
        speed1 = 1  # initial speed of the first car
        speed2 = 1  # initial speed of the second car
        time = 0.0  # total time taken
        
        # Indices for flags
        index1 = 0  # for car 1
        index2 = n - 1  # for car 2
        
        while index1 < n and index2 >= 0:
            # Time until car 1 reaches the next flag or car 2 reaches its flag
            time_to_flag1 = (flags[index1] - pos1) / speed1 if speed1 > 0 else float('inf')
            time_to_flag2 = (pos2 - flags[index2]) / speed2 if speed2 > 0 else float('inf')
            
            if time_to_flag1 < time_to_flag2:
                time += time_to_flag1
                pos1 = flags[index1]
                index1 += 1
                speed1 += 1  # speed increases
                # Now update the position of car 2
                pos2 -= speed2 * time_to_flag1
            else:
                time += time_to_flag2
                pos2 = flags[index2]
                index2 -= 1
                speed2 += 1  # speed increases
                # Now update the position of car 1
                pos1 += speed1 * time_to_flag2
        
        # After all flags are processed, calculate the time until they meet
        if pos1 < pos2:
            remaining_distance = pos2 - pos1
            final_speed1 = speed1
            final_speed2 = speed2
            
            # They are now moving towards each other
            time_to_meet = remaining_distance / (final_speed1 + final_speed2)
            time += time_to_meet
        
        results.append(time)
    
    return results

# Input Reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

for i in range(1, 2 * t, 2):
    n, l = map(int, data[i].split())
    flags = list(map(int, data[i + 1].split()))
    test_cases.append((n, l, flags))

results = time_to_meet(t, test_cases)
for result in results:
    print(f"{result:.12f}")