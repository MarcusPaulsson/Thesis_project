def min_days_to_repair(T, test_cases):
    results = []
    for n, g, b in test_cases:
        # Calculate the minimum number of high-quality pavement needed
        min_high_quality = (n + 1) // 2
        
        # Calculate how many complete cycles of good and bad days are needed
        full_cycles = (min_high_quality - 1) // g
        remaining_good_days = min_high_quality - full_cycles * g
        
        # Calculate total days required
        total_days = full_cycles * (g + b)
        if remaining_good_days > 0:
            total_days += remaining_good_days
        total_days += (n - min_high_quality)  # add remaining units of low-quality days
        
        results.append(max(total_days, n))
    
    return results

# Read input
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Calculate and print results
results = min_days_to_repair(T, test_cases)
for result in results:
    print(result)