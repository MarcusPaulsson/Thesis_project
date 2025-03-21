def solve():
    n = int(input())
    C, T = map(float, input().split())
    problems = []
    for _ in range(n):
        a, p = map(int, input().split())
        problems.append((a, p))
    
    max_score = 0
    
    import itertools
    for perm in itertools.permutations(problems):
        for train_time in range(int(T * 1000) + 1):
            train_time /= 1000.0
            
            if train_time > T:
                continue
            
            current_time = train_time
            current_skill = 1.0 + C * train_time
            current_score = 0
            
            for a, p in perm:
                if current_time + 10 > T:
                    break
                current_time += 10
                current_skill *= 0.9
                
                solve_time = a / current_skill
                if current_time + solve_time > T:
                    break
                current_time += solve_time
                current_score += p
            
            max_score = max(max_score, current_score)
    
    print(int(max_score))

tc = int(input())
for _ in range(tc):
    solve()