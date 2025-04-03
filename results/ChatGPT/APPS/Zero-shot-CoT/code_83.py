def rabbits_meeting(t, test_cases):
    results = []
    for i in range(t):
        x, y, a, b = test_cases[i]
        distance = y - x
        total_hop = a + b
        
        if distance % total_hop == 0:
            results.append(distance // total_hop)
        else:
            results.append(-1)
    
    return results

# Reading input
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = rabbits_meeting(t, test_cases)

# Output results
for result in results:
    print(result)