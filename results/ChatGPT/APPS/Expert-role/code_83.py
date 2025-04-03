def time_to_meet(t, test_cases):
    results = []
    for i in range(t):
        x, y, a, b = test_cases[i]
        distance = y - x
        speed_sum = a + b
        
        if distance % speed_sum == 0:
            results.append(distance // speed_sum)
        else:
            results.append(-1)
    
    return results

# Input handling
t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = time_to_meet(t, test_cases)

for result in results:
    print(result)