def min_time_to_send_presents(t, test_cases):
    results = []
    for case in test_cases:
        n, m, a, b = case
        position = {present: i for i, present in enumerate(a)}
        total_time = 0
        current_top = 0
        
        for present in b:
            pos = position[present]
            # Calculate the number of presents above the current one
            k = pos - current_top
            total_time += 2 * k + 1
            current_top = pos + 1  # Now the top of the stack is above the current present
        
        results.append(total_time)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, m, a, b))

# Get the results
results = min_time_to_send_presents(t, test_cases)

# Output results
for result in results:
    print(result)