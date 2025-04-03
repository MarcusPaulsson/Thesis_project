def solve():
    n, T, a, b = map(int, input().split())
    types = list(map(int, input().split()))
    times = list(map(int, input().split()))

    problems = []
    for i in range(n):
        problems.append((times[i], types[i]))

    max_points = 0
    for leave_time in range(T + 1):
        solved_count = 0
        valid = True
        
        
        sorted_problems = sorted(enumerate(problems), key=lambda x: x[1][0])
        
        solved = [False] * n
        
        time_spent = 0
        
        for i, (time, problem_type) in sorted_problems:
            if time[0] <= leave_time:
                if problem_type == 0:
                    if time_spent + a <= leave_time:
                        time_spent += a
                        solved_count += 1
                        solved[i] = True
                    else:
                        valid = False
                        break
                else:
                    if time_spent + b <= leave_time:
                        time_spent += b
                        solved_count += 1
                        solved[i] = True
                    else:
                        valid = False
                        break
                        
        if valid:
            
            remaining_problems = []
            for i in range(n):
                if not solved[i]:
                    remaining_problems.append((times[i], types[i]))
                    
            
            remaining_problems_sorted = sorted(enumerate(remaining_problems), key=lambda x: x[1][0])
            
            
            for i, (time, problem_type) in remaining_problems_sorted:
                if problem_type == 0:
                    if time_spent + a <= leave_time:
                        time_spent += a
                        solved_count += 1
                    else:
                        break
                else:
                    if time_spent + b <= leave_time:
                        time_spent += b
                        solved_count += 1
                    else:
                        break
            
            
            
            
            
            
            mandatory_solved = True
            for i in range(n):
                if times[i] <= leave_time:
                    
                    if (i not in [idx for idx, _ in sorted_problems]) or not solved[i]:
                        mandatory_solved = False
                        break
                    
            if mandatory_solved:
                max_points = max(max_points, solved_count)
            else:
                pass 
        

    print(max_points)

m = int(input())
for _ in range(m):
    solve()