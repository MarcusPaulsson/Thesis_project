def can_satisfy_customers(test_cases):
    results = []
    for n, m, customers in test_cases:
        current_temp = m
        current_time = 0
        min_temp = m
        max_temp = m
        possible = True
        
        for t, l, h in customers:
            time_passed = t - current_time
            min_temp -= time_passed
            max_temp += time_passed
            
            # Update the temperature range based on the preferred range of the customer
            min_temp = max(min_temp, l)
            max_temp = min(max_temp, h)
            
            if min_temp > max_temp:
                possible = False
                break
            
            current_time = t
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Read input and prepare test cases
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
test_cases = []
index = 1

for _ in range(q):
    n, m = map(int, data[index].split())
    customers = []
    for i in range(n):
        t, l, h = map(int, data[index + 1 + i].split())
        customers.append((t, l, h))
    test_cases.append((n, m, customers))
    index += n + 1

# Get the results
results = can_satisfy_customers(test_cases)

# Print results
for result in results:
    print(result)