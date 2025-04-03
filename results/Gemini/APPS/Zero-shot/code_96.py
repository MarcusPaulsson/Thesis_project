def solve():
    n, T, a, b = map(int, input().split())
    types = list(map(int, input().split()))
    times = list(map(int, input().split()))

    problems = []
    for i in range(n):
        problems.append((times[i], types[i]))

    problems.sort()

    max_points = 0

    for leave_time in range(T + 1):
        solved_count = 0
        time_spent = 0
        
        mandatory_problems = []
        for i in range(n):
            if problems[i][0] <= leave_time:
                mandatory_problems.append(i)

        possible = True
        solved = [False] * n
        
        for i in mandatory_problems:
            if problems[i][1] == 0:
                time_spent += a
            else:
                time_spent += b
            
            if time_spent > leave_time:
                possible = False
                break
            solved[i] = True

        if possible:
            solved_count = len(mandatory_problems)
            
            remaining_problems = []
            for i in range(n):
                if not solved[i]:
                    remaining_problems.append(i)
            
            remaining_problems.sort(key=lambda i: a if problems[i][1] == 0 else b)
            
            for i in remaining_problems:
                if problems[i][1] == 0:
                    if time_spent + a <= leave_time:
                        time_spent += a
                        solved_count += 1
                else:
                    if time_spent + b <= leave_time:
                        time_spent += b
                        solved_count += 1
            
            max_points = max(max_points, solved_count)
    
    print(max_points)

m = int(input())
for _ in range(m):
    solve()