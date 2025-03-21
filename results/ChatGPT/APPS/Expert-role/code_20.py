def can_satisfy_customers(test_cases):
    results = []
    
    for n, m, customers in test_cases:
        current_temp = m
        current_time = 0
        min_temp = m
        max_temp = m
        
        for t_i, l_i, h_i in customers:
            time_diff = t_i - current_time
            
            # Update the possible temperature range
            min_temp -= time_diff
            max_temp += time_diff
            
            # Update the possible range based on customer preference
            min_temp = max(min_temp, l_i)
            max_temp = min(max_temp, h_i)
            
            # If the range is invalid, it's impossible to satisfy this customer
            if min_temp > max_temp:
                results.append("NO")
                break
            
            # Update current time
            current_time = t_i
        else:
            results.append("YES")
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

q = int(data[0])
test_cases = []

index = 1
for _ in range(q):
    n, m = map(int, data[index].split())
    customers = []
    for i in range(1, n + 1):
        t_i, l_i, h_i = map(int, data[index + i].split())
        customers.append((t_i, l_i, h_i))
    test_cases.append((n, m, customers))
    index += n + 1

# Getting results and printing them
results = can_satisfy_customers(test_cases)
for result in results:
    print(result)