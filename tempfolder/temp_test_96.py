def max_points(test_cases):
    results = []
    
    for n, T, a, b, types, times in test_cases:
        easy = []
        hard = []
        
        # Collect easy and hard problems with their respective times
        for i in range(n):
            if types[i] == 0:
                easy.append(times[i])
            else:
                hard.append(times[i])
        
        easy.sort()
        hard.sort()
        
        max_score = 0
        
        # Try to leave the exam at each possible time from 0 to T
        for s in range(T + 1):
            # Count how many problems can be solved by time `s`
            total_easy = 0
            total_hard = 0
            
            # Calculate the time spent on easy problems
            for easy_time in easy:
                if easy_time <= s:
                    total_easy += 1
            
            # Calculate the time spent on hard problems
            for hard_time in hard:
                if hard_time <= s:
                    total_hard += 1
            
            # Check how many can be solved within time `s`
            max_solved = 0
            
            # Maximum problems that can be solved, check easy first
            for e in range(total_easy + 1):
                time_spent = e * a
                remaining_time = s - time_spent
                
                if remaining_time < 0:
                    break
                
                # Calculate how many hard problems can be solved with remaining time
                h = min(total_hard, remaining_time // b)
                max_solved = max(max_solved, e + h)
            
            # Ensure all mandatory problems are solved
            mandatory_count = sum(1 for time in times if time <= s)
            if mandatory_count <= max_solved:
                max_score = max(max_score, max_solved)
        
        results.append(max_score)
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

m = int(data[0])
test_cases = []
index = 1

for _ in range(m):
    n, T, a, b = map(int, data[index].split())
    types = list(map(int, data[index + 1].split()))
    times = list(map(int, data[index + 2].split()))
    test_cases.append((n, T, a, b, types, times))
    index += 3

# Get results
results = max_points(test_cases)

# Print results
for result in results:
    print(result)