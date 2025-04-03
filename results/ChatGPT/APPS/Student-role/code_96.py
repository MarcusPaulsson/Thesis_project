def max_points(test_cases):
    results = []
    for case in test_cases:
        n, T, a, b, problem_types, mandatory_times = case
        easy_problems = []
        hard_problems = []
        
        for i in range(n):
            if problem_types[i] == 0:
                easy_problems.append(mandatory_times[i])
            else:
                hard_problems.append(mandatory_times[i])
        
        easy_problems.sort()
        hard_problems.sort()
        
        max_points = 0
        
        for s in range(T + 1):
            easy_count = 0
            hard_count = 0
            easy_time = 0
            hard_time = 0
            
            for t in easy_problems:
                if t <= s and easy_time + a <= s:
                    easy_time += a
                    easy_count += 1
            
            for t in hard_problems:
                if t <= s and hard_time + b <= s:
                    hard_time += b
                    hard_count += 1
            
            total_count = easy_count + hard_count
            if all(t > s or (easy_time + a > s and hard_time + b > s) for t in mandatory_times if t <= s):
                max_points = max(max_points, total_count)
        
        results.append(max_points)
    
    return results

m = int(input())
test_cases = []

for _ in range(m):
    n, T, a, b = map(int, input().split())
    problem_types = list(map(int, input().split()))
    mandatory_times = list(map(int, input().split()))
    test_cases.append((n, T, a, b, problem_types, mandatory_times))

results = max_points(test_cases)

for result in results:
    print(result)