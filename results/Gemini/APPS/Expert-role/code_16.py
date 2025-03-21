def solve():
    n = int(input())
    c, t = map(float, input().split())
    problems = []
    for _ in range(n):
        a, p = map(int, input().split())
        problems.append((a, p))

    def calculate_score(order, training_time):
        current_time = training_time
        skill = 1.0 + c * training_time
        score = 0
        
        for i in range(len(order)):
            problem_index = order[i]
            a, p = problems[problem_index]
            
            current_time += 10 
            if current_time > t:
                return -1 
            
            skill *= 0.9
            
            current_time += a / skill
            if current_time > t:
                return -1
            
            score += p
        
        return score

    import itertools
    
    max_score = 0
    for order in itertools.permutations(range(n)):
        
        low = 0.0
        high = t
        
        for _ in range(50):
            mid = (low + high) / 2
            
            score = calculate_score(order, mid)
            if score == -1:
                high = mid
            else:
                low = mid
                
        
        best_training_time = low
        score = calculate_score(order, best_training_time)
        if score > max_score:
            max_score = score

    print(int(max_score))

tc = int(input())
for _ in range(tc):
    solve()