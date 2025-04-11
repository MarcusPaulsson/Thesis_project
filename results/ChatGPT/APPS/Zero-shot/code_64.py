n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Prepare a schedule with all days initialized to 0 (rest)
schedule = [0] * n

# To keep track of preparation days needed for each exam
prep_needed = [0] * m

# Fill in the exam days in the schedule
for i in range(m):
    s_i, d_i, c_i = exams[i]
    schedule[d_i - 1] = m + 1  # Mark the exam day (1-indexed to 0-indexed)
    prep_needed[i] = c_i

# Try to allocate preparation days
for i in range(m):
    s_i, d_i, c_i = exams[i]
    days_allocated = 0
    
    for day in range(s_i - 1, d_i - 1):  # s_i to d_i - 1 (0-indexed)
        if schedule[day] == 0 and days_allocated < c_i:  # If it's a rest day
            schedule[day] = i + 1  # Mark preparation for exam i (1-indexed)
            days_allocated += 1
    
    if days_allocated < c_i:  # If we couldn't allocate enough preparation days
        print(-1)
        exit()

# Print the final schedule
print(" ".join(map(str, schedule)))