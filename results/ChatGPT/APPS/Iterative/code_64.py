def schedule_exams(n, m, exams):
    # Prepare the schedule with zeros
    schedule = [0] * n
    
    # Prepare to track available days for preparation
    available_days = [0] * n
    
    # Fill the available days for preparation
    for s_i, d_i, c_i in exams:
        for day in range(s_i - 1, d_i - 1):  # from s_i to d_i-1
            available_days[day] += 1
    
    # Try to allocate preparation days
    for exam_index, (s_i, d_i, c_i) in enumerate(exams):
        days_needed = c_i
        
        for day in range(s_i - 1, d_i - 1):
            if schedule[day] == 0 and days_needed > 0:
                schedule[day] = exam_index + 1  # Prepare for exam exam_index
                days_needed -= 1
        
        if days_needed > 0:
            return -1  # Not enough preparation days
    
    return schedule

# Input reading
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Output result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))