def schedule_exams(n, m, exams):
    # Create a schedule list initialized with rest days
    schedule = [0] * n
    
    # Sort exams by their exam day for easier management
    exams.sort(key=lambda x: x[1])  # Sort by exam day (d_i)
    
    # Prepare a list to track the preparation days needed
    prep_needed = [0] * (n + 1)
    
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        prep_needed[i + 1] = c_i  # Store the required preparation days for each exam
    
    # Attempt to fill the schedule
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        prep_days = 0
        
        # Try to allocate preparation days
        for day in range(s_i - 1, d_i - 1):
            if prep_needed[i + 1] > 0 and schedule[day] == 0:
                schedule[day] = i + 1  # Mark preparation for exam i
                prep_needed[i + 1] -= 1
                prep_days += 1

        # If we didn't manage to allocate enough preparation days
        if prep_needed[i + 1] > 0:
            return -1

        # Now mark the day of the exam
        schedule[d_i - 1] = m + 1  # Mark the exam day

    return schedule

# Read input
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result
result = schedule_exams(n, m, exams)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))