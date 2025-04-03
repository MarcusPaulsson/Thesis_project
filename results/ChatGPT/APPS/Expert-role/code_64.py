def time_to_meet(test_cases):
    results = []
    for n, l, flags in test_cases:
        left_speed = 1.0
        right_speed = 1.0
        left_position = 0.0
        right_position = l
        time = 0.0
        
        flags = [0] + flags + [l]  # Add start and end positions as flags
        
        for i in range(1, len(flags)):
            left_time_to_flag = (flags[i] - left_position) / left_speed
            right_time_to_flag = (right_position - flags[-i]) / right_speed
            
            if left_time_to_flag < right_time_to_flag:
                time += left_time_to_flag
                left_position = flags[i]
                left_speed += 1.0
                right_position -= right_speed * left_time_to_flag
                right_speed += 0.0  # Right car speed remains the same
            else:
                time += right_time_to_flag
                right_position = flags[-i]
                right_speed += 1.0
                left_position += left_speed * right_time_to_flag
                left_speed += 0.0  # Left car speed remains the same
            
            # Check if they meet before reaching the next flag
            if left_position >= right_position:
                # They meet
                time += (right_position - left_position) / (left_speed + right_speed)
                break
        
        results.append(f"{time:.12f}")
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n, l = map(int, data[index].split())
    flags = list(map(int, data[index + 1].split()))
    test_cases.append((n, l, flags))
    index += 2

# Getting results
results = time_to_meet(test_cases)

# Output results
print("\n".join(results))