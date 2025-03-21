def max_score(tc, test_cases):
    results = []
    
    for case in test_cases:
        n, (C, T), problems = case
        max_possible_score = 0
        
        # Iterate over all combinations of problems
        for mask in range(1 << n):
            current_time = 0
            current_score = 0
            s = 1.0
            
            # Count how many problems are selected
            selected_problems = []
            for i in range(n):
                if mask & (1 << i):
                    selected_problems.append(problems[i])
                    
            # Calculate the time for training
            total_problems = len(selected_problems)
            if total_problems > 0:
                # Training time
                training_time = (T - total_problems * 10) / (C + total_problems * 0.9)
                if training_time < 0:
                    continue
                s += C * training_time
            
            # Reset current time for problem solving after training
            current_time = training_time
            
            for a_i, p_i in selected_problems:
                # Time for watching an episode
                current_time += 10
                if current_time > T:
                    break
                
                # Update skill after watching the episode
                s *= 0.9
                
                # Time required to solve the problem
                time_to_solve = a_i / s
                current_time += time_to_solve
                
                if current_time > T:
                    break
                
                # Add the score of the problem
                current_score += p_i
            
            max_possible_score = max(max_possible_score, current_score)
        
        results.append(max_possible_score)
    
    return results


# Read input and process
import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
tc = int(data[index])
index += 1
test_cases = []

for _ in range(tc):
    n = int(data[index])
    index += 1
    C, T = map(float, data[index].split())
    index += 1
    problems = []
    for _ in range(n):
        a_i, p_i = map(int, data[index].split())
        problems.append((a_i, p_i))
        index += 1
    test_cases.append((n, (C, T), problems))

results = max_score(tc, test_cases)
for result in results:
    print(result)