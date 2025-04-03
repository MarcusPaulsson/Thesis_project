def can_satisfy_customers(q, test_cases):
    results = []
    
    for case in test_cases:
        n, m, customers = case
        current_time = 0
        current_temp_range = (m, m)  # Initial temperature range
        
        for t_i, l_i, h_i in customers:
            # Time difference between current time and the customer's time
            time_diff = t_i - current_time
            
            # Update the temperature range based on time passed
            current_temp_range = (
                current_temp_range[0] - time_diff,  # Cooling
                current_temp_range[1] + time_diff   # Heating
            )
            
            # Update the current time
            current_time = t_i
            
            # The new temperature range must intersect with the customer's preferred range
            new_range_start = max(current_temp_range[0], l_i)
            new_range_end = min(current_temp_range[1], h_i)
            
            if new_range_start > new_range_end:  # No intersection
                results.append("NO")
                break
        else:
            results.append("YES")
    
    return results

# Input processing
q = int(input())
test_cases = []

for _ in range(q):
    n, m = map(int, input().split())
    customers = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, customers))

# Get the results
results = can_satisfy_customers(q, test_cases)

# Output results
for result in results:
    print(result)