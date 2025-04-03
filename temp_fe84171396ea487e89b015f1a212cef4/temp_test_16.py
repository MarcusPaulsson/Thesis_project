def solve():
    n = int(input())
    C, T = map(float, input().split())
    problems = []
    for _ in range(n):
        a, p = map(int, input().split())
        problems.append((a, p))

    def calculate_score(order, training_time):
        s = 1.0 + C * training_time
        time_spent = training_time
        total_score = 0
        
        for problem_index in order:
            a, p = problems[problem_index]
            
            time_spent += 10 
            if time_spent > T:
                return -1
            
            time_spent += a / s
            if time_spent > T:
                return -1
            
            total_score += p
            s *= 0.9
            
        return total_score

    import itertools
    
    max_score = 0
    for order in itertools.permutations(range(n)):
        
        low = 0.0
        high = T
        
        for _ in range(50):
            mid = (low + high) / 2
            score = calculate_score(order, mid)
            
            if score == -1:
                high = mid
            else:
                low = mid
        
        max_score = max(max_score, calculate_score(order, low))

    print(max_score)

tc = int(input())
for _ in range(tc):
    solve()