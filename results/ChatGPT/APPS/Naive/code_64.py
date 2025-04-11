def schedule_exams(n, m, exams):
    # Initialize the schedule with zeros (rest days)
    schedule = [0] * n
    # To keep track of preparation days needed for each exam
    preparation_needed = [0] * m
    
    # Fill the exam days in the schedule
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        schedule[d_i - 1] = m + 1  # Exam day (1-indexed)
        preparation_needed[i] = c_i

    # Prepare for exams
    for i in range(m):
        s_i, d_i, c_i = exams[i]
        days_prepared = 0
        
        for j in range(s_i - 1, d_i - 1):
            if schedule[j] == 0 and days_prepared < c_i:
                schedule[j] = i + 1  # Prepare for exam i (1-indexed)
                days_prepared += 1

        if days_prepared < c_i:
            return -1  # Not enough preparation days

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