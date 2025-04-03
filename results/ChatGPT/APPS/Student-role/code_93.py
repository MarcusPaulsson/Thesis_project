def minimum_time_to_send_presents(test_cases):
    results = []
    
    for n, m, a, b in test_cases:
        # Create a mapping of present number to its index in the stack
        position = {present: i for i, present in enumerate(a)}
        
        # Time initialization
        total_time = 0
        current_index = -1  # Start above the stack

        for present in b:
            target_index = position[present]
            # Calculate how many presents are above the target present
            if target_index > current_index:
                k = target_index - current_index - 1
                total_time += 2 * k + 1
                current_index = target_index

        results.append(total_time)
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, m, a, b))

# Get results
results = minimum_time_to_send_presents(test_cases)

# Print results
for result in results:
    print(result)