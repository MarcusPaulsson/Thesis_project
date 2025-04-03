def max_points(test_cases):
    results = []
    for n, T, a, b, problems, mandatory_times in test_cases:
        easy_problems = []
        hard_problems = []
        
        for i in range(n):
            if problems[i] == 0:
                easy_problems.append((mandatory_times[i], a))
            else:
                hard_problems.append((mandatory_times[i], b))
        
        easy_problems.sort()  # Sort by mandatory time
        hard_problems.sort()  # Sort by mandatory time
        
        total_points = 0
        time_used = 0
        
        # Function to calculate maximum problems solved
        def calculate_max_solved(problems, time_limit):
            count = 0
            current_time = 0
            for _, time_needed in problems:
                if current_time + time_needed <= time_limit:
                    current_time += time_needed
                    count += 1
                else:
                    break
            return count
        
        # Check for each possible leave time from 0 to T
        for leave_time in range(T + 1):
            # Find mandatory problems to solve
            mandatory_easy = [p for p in easy_problems if p[0] <= leave_time]
            mandatory_hard = [p for p in hard_problems if p[0] <= leave_time]
            
            # Calculate points
            total_easy = calculate_max_solved(easy_problems, leave_time)
            total_hard = calculate_max_solved(hard_problems, leave_time)
            
            # Check if all mandatory problems are solved
            if len(mandatory_easy) <= total_easy and len(mandatory_hard) <= total_hard:
                total_points = max(total_points, total_easy + total_hard)
        
        results.append(total_points)
    
    return results

# Reading input
m = int(input())
test_cases = []
for _ in range(m):
    n, T, a, b = map(int, input().split())
    problems = list(map(int, input().split()))
    mandatory_times = list(map(int, input().split()))
    test_cases.append((n, T, a, b, problems, mandatory_times))

# Getting results
results = max_points(test_cases)

# Printing output
for result in results:
    print(result)