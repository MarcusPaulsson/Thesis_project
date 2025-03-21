def solve():
    n = int(input())
    C, T = map(float, input().split())
    problems = []
    for _ in range(n):
        a, p = map(int, input().split())
        problems.append((a, p))

    max_score = 0

    for i in range(1 << n):
        selected_problems = []
        for j in range(n):
            if (i >> j) & 1:
                selected_problems.append(problems[j])

        import itertools
        
        for perm in itertools.permutations(selected_problems):
            
            for training_time in range(int(T * 1000) + 1):
                training_time /= 1000.0
                
                current_time = training_time
                current_skill = 1.0 + C * training_time
                current_score = 0
                
                
                valid = True
                for a, p in perm:
                    current_time += 10.0
                    if current_time > T:
                        valid = False
                        break
                    
                    current_time += a / current_skill
                    if current_time > T:
                        valid = False
                        break
                    
                    current_score += p
                    current_skill *= 0.9
                    
                if valid:
                    max_score = max(max_score, current_score)

    print(int(max_score))


tc = int(input())
for _ in range(tc):
    solve()