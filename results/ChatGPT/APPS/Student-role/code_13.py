def min_days_to_repair(T, cases):
    results = []
    for n, g, b in cases:
        # Calculate the minimum high-quality units needed
        min_high_quality = (n + 1) // 2
        
        # Calculate the number of full cycles needed and remaining days
        full_cycles = (min_high_quality + g - 1) // g
        remaining_high_quality = min_high_quality - (full_cycles - 1) * g
        
        # Total days needed including the bad days
        total_days = (full_cycles - 1) * (g + b) + remaining_high_quality
        
        # The total days cannot be less than n
        results.append(max(n, total_days))
    
    return results

# Read input
T = int(input())
cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = min_days_to_repair(T, cases)

# Print results
for result in results:
    print(result)