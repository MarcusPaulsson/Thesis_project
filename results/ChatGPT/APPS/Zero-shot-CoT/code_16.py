def max_score(tc, test_cases):
    results = []
    
    for case in test_cases:
        n, (C, T), problems = case
        problems.sort(key=lambda x: (-x[1] / (x[0] / 1.0), x[0]))  # sort by score/difficulty ratio and then by difficulty
        
        max_score = 0
        
        for training_time in range(int(T) + 1):
            if training_time % 10 != 0:
                continue
            
            # Calculate the new skill after training
            s = 1.0 + C * (training_time / 60.0)  # Convert training_time to hours for C
            
            total_time = training_time
            score = 0
            
            for a_i, p_i in problems:
                if total_time + 10 > T:
                    break  # Not enough time to watch the episode
                
                total_time += 10  # Watch an episode
                s *= 0.9  # Skill decreases by 10%
                
                time_needed = a_i / s
                if total_time + time_needed > T:
                    break  # Not enough time to solve the problem
                
                total_time += time_needed
                score += p_i
            
            max_score = max(max_score, score)
        
        results.append(max_score)
    
    return results


# Input reading and function calling
tc = int(input())
test_cases = []
for _ in range(tc):
    n = int(input())
    C, T = map(float, input().split())
    problems = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, (C, T), problems))

results = max_score(tc, test_cases)
for result in results:
    print(result)