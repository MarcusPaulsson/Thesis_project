def max_points(test_cases):
    results = []
    for n, T, a, b, problem_types, mandatory_times in test_cases:
        problems = [(problem_types[i], mandatory_times[i]) for i in range(n)]
        problems.sort(key=lambda x: x[1])  # Sort by mandatory times
        
        easy_problems = [t for t, _ in problems if t == 0]
        hard_problems = [t for t, _ in problems if t == 1]
        
        max_points = 0
        
        # Iterate through possible leave times
        for leave_time in range(T + 1):
            total_time = 0
            solved_problems = 0
            
            # Solve mandatory problems first
            for p_type, m_time in problems:
                if m_time > leave_time:
                    break
                if p_type == 0:  # Easy problem
                    if total_time + a <= leave_time:
                        total_time += a
                        solved_problems += 1
                else:  # Hard problem
                    if total_time + b <= leave_time:
                        total_time += b
                        solved_problems += 1
            
            # Update max points
            max_points = max(max_points, solved_problems)
        
        results.append(max_points)
    
    return results

# Read input
m = int(input())
test_cases = []
for _ in range(m):
    n, T, a, b = map(int, input().split())
    problem_types = list(map(int, input().split()))
    mandatory_times = list(map(int, input().split()))
    test_cases.append((n, T, a, b, problem_types, mandatory_times))

# Get results
results = max_points(test_cases)

# Print results
for result in results:
    print(result)