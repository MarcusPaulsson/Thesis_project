def rabbits_meeting(t, test_cases):
    results = []
    for i in range(t):
        x, y, a, b = test_cases[i]
        distance = y - x
        total_speed = a + b
        
        if distance % total_speed == 0:
            results.append(distance // total_speed)
        else:
            results.append(-1)
    
    return results

# Read input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

# Get results
results = rabbits_meeting(t, test_cases)

# Print output
for result in results:
    print(result)