def min_crossroad_to_board(t, test_cases):
    results = []
    for case in test_cases:
        a, b, p, s = case
        n = len(s)
        
        total_cost = 0
        last_type = s[0]
        
        # Calculate the total cost from the first crossroad to the last
        for i in range(1, n):
            if s[i] != last_type:
                if last_type == 'A':
                    total_cost += a
                else:
                    total_cost += b
                last_type = s[i]
        
        # Find the minimal index to start
        current_cost = 0
        for i in range(n):
            if i > 0 and s[i] != s[i - 1]:
                if s[i - 1] == 'A':
                    current_cost += a
                else:
                    current_cost += b
            
            if total_cost - current_cost <= p:
                results.append(i + 1)
                break

    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    a, b, p = map(int, input().split())
    s = input().strip()
    test_cases.append((a, b, p, s))

# Process the test cases
results = min_crossroad_to_board(t, test_cases)

# Output the results
for result in results:
    print(result)