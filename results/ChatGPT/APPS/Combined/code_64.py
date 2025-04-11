def schedule_exams(n, m, exams):
    # Initialize the schedule with zeros (rest days)
    schedule = [0] * n
    
    # Try to allocate preparation days
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        days_allocated = 0
        
        # Allocate preparation days between s_i and d_i - 1
        for day in range(s_i - 1, d_i - 1):
            if days_allocated < c_i and schedule[day] == 0:
                schedule[day] = i + 1  # Mark the day for preparation for exam i
                days_allocated += 1
        
        # If we couldn't allocate enough preparation days, return -1
        if days_allocated < c_i:
            return -1
    
    # Now allocate the exam days
    for i in range(m):
        d_i = exams[i][1]
        schedule[d_i - 1] = m + 1  # Mark the exam day
    
    return schedule

# Read input
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))