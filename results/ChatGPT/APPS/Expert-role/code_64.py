def schedule_exams(n, m, exams):
    # Create a schedule initialized to rest days
    schedule = [0] * n
    
    # Sort exams by their exam day
    exams = sorted(exams, key=lambda x: x[1])
    
    # Keep track of preparation days needed
    preparation_needed = [0] * m
    
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        preparation_needed[i] = c_i  # days needed for preparation
        # Mark the exam day
        schedule[d_i - 1] = m + 1  # m + 1 indicates it's an exam day
    
    # Try to allocate preparation days
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        days_allocated = 0
        
        # Allocate preparation days from s_i to d_i - 1
        for j in range(s_i - 1, d_i - 1):
            if days_allocated < c_i and schedule[j] == 0:
                schedule[j] = i + 1  # Mark as preparing for exam i + 1
                days_allocated += 1
        
        # Check if we allocated enough preparation days
        if days_allocated < c_i:
            return -1  # Not enough preparation days

    return schedule

# Read input
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Print output
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))