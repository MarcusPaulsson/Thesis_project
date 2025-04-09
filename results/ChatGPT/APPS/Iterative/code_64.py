n, m = map(int, input().split())
exams = [tuple(map(int, input().split())) for _ in range(m)]

# Prepare the schedule
schedule = [0] * n  # Initialize all days with rest (0)
exam_days = set()   # Store exam days

# Mark the exam days in the schedule
for i in range(m):
    s_i, d_i, c_i = exams[i]
    schedule[d_i - 1] = m + 1  # Mark the exam day (1-indexed)
    exam_days.add(d_i)

# Prepare for each exam
for i in range(m):
    s_i, d_i, c_i = exams[i]
    prepared_days = 0

    # Try to allocate preparation days
    for day in range(s_i - 1, d_i - 1):
        if prepared_days < c_i and schedule[day] == 0:  # If it's a rest day
            schedule[day] = i + 1  # Mark preparation for exam i
            prepared_days += 1

    if prepared_days < c_i:  # Not enough preparation days
        print(-1)
        exit()

# Check if all exams can be passed
for i in range(m):
    if schedule[exams[i][1] - 1] != m + 1:  # Ensure exam day is marked
        print(-1)
        exit()

print(' '.join(map(str, schedule)))