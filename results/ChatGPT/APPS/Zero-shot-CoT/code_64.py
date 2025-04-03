def schedule_exams(n, m, exams):
    days = [0] * n  # Initialize days with 0 (rest days)
    
    # Sort exams based on the day of the exam
    exams.sort(key=lambda x: x[1])
    
    # Preparation tracking
    preparation_days = [0] * m  # How many days are allocated for preparation for each exam
    exam_days = [0] * m  # When exams are scheduled 

    for i in range(m):
        s_i, d_i, c_i = exams[i]
        s_i -= 1  # Convert to 0-indexed
        d_i -= 1  # Convert to 0-indexed
        exam_days[i] = d_i
        
        # Try to allocate preparation days
        count = 0
        for j in range(s_i, d_i):
            if days[j] == 0 and count < c_i:  # Only prepare on rest days
                days[j] = i + 1  # Marking preparation for exam i
                count += 1
        
        preparation_days[i] = count
        
        # If we couldn't allocate enough preparation days, return -1
        if count < c_i:
            return -1
    
    # Mark exam days
    for i in range(m):
        days[exam_days[i]] = m + 1  # Marking exam day
    
    return days

# Read input
n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Get the schedule
result = schedule_exams(n, m, exams)

# Print the result
if result == -1:
    print(result)
else:
    print(' '.join(map(str, result)))