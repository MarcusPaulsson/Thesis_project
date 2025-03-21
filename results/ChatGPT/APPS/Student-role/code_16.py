def max_score(tc, test_cases):
    results = []
    
    for case in test_cases:
        n, (C, T), problems = case
        problems.sort(key=lambda x: x[1], reverse=True)  # Sort by score descending
        
        max_score = 0
        
        for train_time in range(int(T // 10) + 1):  # Number of episodes watched
            time_spent = train_time * 10
            if time_spent > T:
                continue
            
            score = 0
            current_skill = 1.0 + C * (T - time_spent) / 60.0  # max possible skill after training
            
            for i in range(train_time):
                current_skill *= 0.9  # Decrease skill after each episode
            
            for problem in problems:
                a_i, p_i = problem
                watch_time = 10
                solve_time = a_i / current_skill
                
                if time_spent + watch_time + solve_time > T:
                    continue
                
                time_spent += watch_time + solve_time
                score += p_i
                current_skill *= 0.9  # Decrease skill after solving
                
            max_score = max(max_score, score)
        
        results.append(max_score)
    
    return results

# Input reading
tc = int(input())
test_cases = []

for _ in range(tc):
    n = int(input())
    C, T = map(float, input().split())
    problems = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, (C, T), problems))

results = max_score(tc, test_cases)

for res in results:
    print(res)