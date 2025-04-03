def min_time_to_send_presents(t, test_cases):
    results = []
    for case in test_cases:
        n, m, presents_stack, presents_to_send = case
        position = {presents_stack[i]: i for i in range(n)}
        
        time_spent = 0
        current_top = n
        
        for present in presents_to_send:
            idx = position[present]
            k = current_top - idx - 1  # Number of presents above the current present
            time_spent += 2 * k + 1  # Time to take and return presents
            current_top = idx  # Update the new top position
        
        results.append(time_spent)
    
    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    presents_stack = list(map(int, input().split()))
    presents_to_send = list(map(int, input().split()))
    test_cases.append((n, m, presents_stack, presents_to_send))

# Get results
results = min_time_to_send_presents(t, test_cases)

# Print results
for result in results:
    print(result)