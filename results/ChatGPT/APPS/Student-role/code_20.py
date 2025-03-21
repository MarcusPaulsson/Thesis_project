def can_satisfy_customers(test_cases):
    results = []
    
    for case in test_cases:
        n, m, customers = case
        current_time = 0
        current_temp_range = (m, m)  # initial temperature range
        
        for t_i, l_i, h_i in customers:
            time_passed = t_i - current_time
            
            # Update the temperature range based on time passed
            new_temp_range = (
                current_temp_range[0] - time_passed,  # cooling
                current_temp_range[1] + time_passed   # heating
            )
            
            # Update to the intersection with the customer's preferred range
            new_temp_range = (
                max(new_temp_range[0], l_i),
                min(new_temp_range[1], h_i)
            )
            
            # If the new range is invalid, we can't satisfy this customer
            if new_temp_range[0] > new_temp_range[1]:
                results.append("NO")
                break
            
            # Update the current time and temperature range
            current_time = t_i
            current_temp_range = new_temp_range
            
        else:
            # If we didn't break from the loop, all customers satisfied
            results.append("YES")
    
    return results


# Read input
import sys

input = sys.stdin.read
data = input().strip().split('\n')
q = int(data[0].strip())
index = 1
test_cases = []

for _ in range(q):
    n, m = map(int, data[index].strip().split())
    index += 1
    customers = []
    
    for _ in range(n):
        t_i, l_i, h_i = map(int, data[index].strip().split())
        customers.append((t_i, l_i, h_i))
        index += 1
        
    test_cases.append((n, m, customers))

# Get results
results = can_satisfy_customers(test_cases)

# Print results
for result in results:
    print(result)