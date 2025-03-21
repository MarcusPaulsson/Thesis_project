def min_days_to_repair(T, test_cases):
    results = []
    for n, g, b in test_cases:
        required_good = (n + 1) // 2  # At least half should be high quality
        full_cycles = required_good // g
        remaining_good = required_good % g
        
        if remaining_good == 0:
            total_days = full_cycles * (g + b) - b
        else:
            total_days = full_cycles * (g + b) + remaining_good
            
        total_days = max(total_days, n)  # Ensure total days is at least n
        
        results.append(total_days)
    
    return results

# Read input
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = min_days_to_repair(T, test_cases)

# Print results
for result in results:
    print(result)