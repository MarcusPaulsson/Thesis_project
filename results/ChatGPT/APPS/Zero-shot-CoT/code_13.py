def min_days_to_repair_highway(test_cases):
    results = []
    for n, g, b in test_cases:
        # Calculate the minimum high-quality pavement needed
        high_quality_needed = (n + 1) // 2
        
        # Calculate how many full cycles of good and bad days are needed
        full_cycles_needed = (high_quality_needed + g - 1) // g
        total_days = full_cycles_needed * (g + b)  # Total days for full cycles
        
        # Calculate how many high-quality days we can actually use
        high_quality_days_used = full_cycles_needed * g
        
        # If we have used enough high-quality days, we need to check if we need more days
        if high_quality_days_used >= high_quality_needed:
            total_days -= (high_quality_days_used - high_quality_needed)
        else:
            # We need to account for the remaining high-quality days after full cycles
            remaining_high_quality_needed = high_quality_needed - high_quality_days_used
            total_days += remaining_high_quality_needed  # Add the needed high-quality days

        # Make sure we do not exceed the total length of the highway
        total_days = max(total_days, n)
        
        results.append(total_days)
    
    return results


# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get the results
results = min_days_to_repair_highway(test_cases)

# Output results
for result in results:
    print(result)