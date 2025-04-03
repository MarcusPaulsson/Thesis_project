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
        possible = True
        
        mandatory_problems = []
        non_mandatory_problems = []

        for i in range(n):
            if problems[i][0] <= leave_time:
                mandatory_problems.append(problems[i])
            else:
                non_mandatory_problems.append(problems[i])
        
        mandatory_problems.sort()
        non_mandatory_problems.sort()
            
        time_spent = 0
        solved_mandatory = 0
        
        for problem in mandatory_problems:
            if problem[1] == 0:
                solve_time = a
            else:
                solve_time = b
                
            if time_spent + solve_time <= leave_time:
                time_spent += solve_time
                solved_mandatory += 1
            else:
                possible = False
                break
        
        if not possible:
            continue
        
        solved_count += solved_mandatory
        
        remaining_time = leave_time - time_spent
        
        
        
        easy_count = 0
        hard_count = 0
        for i in range(n):
            if types[i] == 0:
                easy_count +=1
            else:
                hard_count +=1

        
        easy_solved = 0
        hard_solved = 0
        
        
        remaining_problems = []
        for problem in non_mandatory_problems:
            remaining_problems.append(problem[1])
            
        
        
        
        
        
        temp_solved = 0
        temp_time = 0
        
        easy_remaining = remaining_problems.count(0)
        hard_remaining = remaining_problems.count(1)

        
        
        while temp_time + a <= remaining_time and easy_remaining > 0:
            temp_time += a
            temp_solved += 1
            easy_remaining -= 1
            
        while temp_time + b <= remaining_time and hard_remaining > 0:
            temp_time += b
            temp_solved += 1
            hard_remaining -= 1
            
        
        
        solved_count += temp_solved
        

        max_points = max(max_points, solved_count)

    print(max_points)

m = int(input())
for _ in range(m):
    solve()