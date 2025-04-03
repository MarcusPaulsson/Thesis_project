def solve():
    n, T, a, b = map(int, input().split())
    types = list(map(int, input().split()))
    times = list(map(int, input().split()))
    
    problems = []
    for i in range(n):
        problems.append((times[i], types[i]))
    
    problems.sort()
    
    max_solved = 0
    
    for leave_time in range(T + 1):
        solved_count = 0
        possible = True
        
        solved_indices = []
        
        for i in range(n):
            if problems[i][0] <= leave_time:
                solved_indices.append(i)
        
        
        
        for i in range(n):
            if problems[i][0] <= leave_time:
                pass
            else:
                continue
            
        
        
        for i in range(1 << n):
            current_solved_count = 0
            current_time = 0
            current_solved_indices = []
            
            for j in range(n):
                if (i >> j) & 1:
                    current_solved_indices.append(j)
            
            valid_solution = True
            
            
            mandatory_solved = True
            for j in range(n):
                if problems[j][0] <= leave_time:
                    if j not in current_solved_indices:
                         mandatory_solved = False
                         break
            
            
            if not mandatory_solved:
                continue
            
            
            
            
            
            current_solved_count = len(current_solved_indices)
            
            for j in range(len(current_solved_indices)):
                problem_index = current_solved_indices[j]
                
                if problems[problem_index][1] == 0:
                    current_time += a
                else:
                    current_time += b
                    
                if current_time > leave_time:
                    valid_solution = False
                    break
            
            if valid_solution:
                max_solved = max(max_solved, current_solved_count)

    print(max_solved)

t = int(input())
for _ in range(t):
    solve()