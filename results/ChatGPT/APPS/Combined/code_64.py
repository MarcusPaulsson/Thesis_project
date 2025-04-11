def schedule_exams(n, m, exams):
    # Initialize the schedule with zeros (rest days)
    schedule = [0] * n
    
    # Process each exam
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        # Adjust to 0-based index
        s_i -= 1
        d_i -= 1
        
        # Find available preparation days
        available_days = [j for j in range(s_i, d_i) if schedule[j] == 0]
        
        # Check if we can allocate preparation days
        if len(available_days) < c_i:
            return -1  # Not enough days to prepare
        
        # Allocate preparation days
        for j in range(c_i):
            schedule[available_days[j]] = i + 1  # Mark preparation for exam i+1
        
        # Mark the exam day
        schedule[d_i] = m + 1  # Mark the exam day
    
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